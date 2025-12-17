# players/models.py
from django.contrib import admin
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Player(models.Model):
    TOUR_CHOICES = [
        ('ATP', 'ATP'),
        ('WTA', 'WTA'),
        ('ITF', 'ITF'),
    ]

    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)
    tour = models.CharField(max_length=10, choices=TOUR_CHOICES)
    external_api_id = models.CharField(max_length=100, unique=True)
    ranking = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'players'
        ordering = ['name']

    def __str__(self):
        return self.name


class FavouritePlayer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favourite_players'
    )
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='favourited_by'
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'favourite_players'
        unique_together = ('user', 'player')
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.user.username} -> {self.player.name}"
