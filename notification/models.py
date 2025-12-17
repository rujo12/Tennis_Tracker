# notifications/models.py

from django.db import models
from django.contrib.auth import get_user_model
from matches.models import Match

User = get_user_model()


class NotificationPreference(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='notification_preference'
    )
    email_enabled = models.BooleanField(default=True)
    minutes_before = models.IntegerField(
        default=60,
        help_text='Minutes before match to send alert'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notification_preferences'

    def __str__(self):
        return f"Preferences - {self.user.email}"


class NotificationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    notification_type = models.CharField(
        max_length=20,
        choices=[('email', 'Email'), ('sms', 'SMS')]
    )
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('sent', 'Sent'), ('failed', 'Failed')]
    )

    class Meta:
        db_table = 'notification_logs'

