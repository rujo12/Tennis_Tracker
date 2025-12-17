from rest_framework import serializers
from .models import Match
from players.serializers import PlayerSerializer


class MatchSerializer(serializers.ModelSerializer):
    player1_details = PlayerSerializer(source='player1', read_only=True)
    player2_details = PlayerSerializer(source='player2', read_only=True)

    class Meta:
        model = Match
        fields = (
            'id',
            'player1',
            'player1_details',
            'player2',
            'player2_details',
            'tournament_name',
            'tournament_level',
            'match_date',
            'court',
            'status',
            'score',
            'created_at',
        )
        read_only_fields = ('id', 'created_at')
