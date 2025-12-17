# matches/models.py
from django.contrib import admin
from django.db import models
from players.models import Player


class Match(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('live', 'Live'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    player1 = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='matches_as_p1'
    )
    player2 = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='matches_as_p2'
    )
    tournament_name = models.CharField(max_length=255)
    tournament_level = models.CharField(
        max_length=50,
        choices=[
            ('Grand Slam', 'Grand Slam'),
            ('ATP 1000', 'ATP 1000'),
            ('ATP 500', 'ATP 500'),
            ('ATP 250', 'ATP 250'),
            ('Others', 'Others'),
        ],
        default='Others'
    )
    match_date = models.DateTimeField()
    court = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='scheduled'
    )
    external_match_id = models.CharField(max_length=100, unique=True)
    score = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'matches'
        ordering = ['match_date']

    def __str__(self):
        return f"{self.player1.name} vs {self.player2.name} - {self.tournament_name}"

