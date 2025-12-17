
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    timezone = models.CharField(
        max_length=50,
        default='UTC',
        help_text='e.g., America/New_York, Europe/London'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email or self.username

