from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Player, FavouritePlayer
from .serializers import PlayerSerializer,FavouritePlayerSerializer


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'country']
    filterset_fields = ['tour']


class FavouritePlayerViewSet(viewsets.ModelViewSet):
    serializer_class = FavouritePlayerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavouritePlayer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['POST'])
    def bulk_add(self, request):
        player_ids = request.data.get('player_ids', [])
        user = request.user

        for player_id in player_ids:
            FavouritePlayer.objects.get_or_create(user=user, player_id=player_id)

        return Response({'status': 'Players added'}, status=status.HTTP_201_CREATED)
