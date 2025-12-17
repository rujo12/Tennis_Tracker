from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from matches.models import Match
from notification.models import NotificationPreference
from datetime import timedelta
from django.db.models import Q

User = get_user_model()


@shared_task
def send_match_reminders():
    now = timezone.now()
    print("Running reminder task at:", now)

    users = User.objects.all()

    for user in users:
        try:
            pref = user.notification_preference
        except NotificationPreference.DoesNotExist:
            print(f"Skipping {user.username} – no notification preference")
            continue

        if not pref.email_enabled:
            print(f"Skipping {user.username} – email disabled")
            continue

        reminder_time = now + timedelta(minutes=pref.minutes_before)

        favourite_ids = list(user.favourite_players.values_list('player_id', flat=True))
        if not favourite_ids:
            print(f"Skipping {user.username} – no favourite players")
            continue

        # Matches for upcoming favourites within reminder window
        matches = Match.objects.filter(
            status='scheduled',
            match_date__gte=now,
            match_date__lte=reminder_time
        ).filter(
            Q(player1_id__in=favourite_ids) | Q(player2_id__in=favourite_ids)
        )

        if not matches.exists():
            print(f"No upcoming matches for {user.username}")
            continue

        for match in matches:
            send_email_reminder(user, match)
            print(f"Email sent to {user.email} for match {match}")


def send_email_reminder(user, match):
    subject = f"Match Reminder: {match.player1.name} vs {match.player2.name}"

    message = f"""
Hi {user.first_name or user.username},

Your favourite player has an upcoming match!

{match.player1.name} vs {match.player2.name}
Tournament: {match.tournament_name}
Date & Time: {match.match_date.astimezone()}
Court: {match.court or 'TBD'}

Don't miss it!
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
