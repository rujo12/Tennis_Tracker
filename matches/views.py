from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.db import models

from .models import Match
from .serializers import MatchSerializer


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['tournament_level', 'status']
    ordering_fields = ['match_date']
    ordering = ['match_date']

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def my_schedule(self, request):
        user = request.user
        favourite_players = user.favourite_players.values_list('player_id', flat=True)
        upcoming_matches = Match.objects.filter(
            status='scheduled'
        ).filter(
            models.Q(player1_id__in=favourite_players) | models.Q(player2_id__in=favourite_players)
        ).order_by('match_date')
        serializer = self.get_serializer(upcoming_matches, many=True)
        return Response(serializer.data)

