import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('tennis_tracker')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch-matches-every-30-min': {
        'task': 'notification.tasks.fetch_upcoming_matches',
        'schedule': crontab(minute='*/30'),
    },
    'send-reminders-every-5-min': {
        'task': 'notification.tasks.send_match_reminders',
        'schedule': crontab(minute='*/5'),
    },
}
