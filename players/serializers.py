from rest_framework import serializers
from .models import Player, FavouritePlayer


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'country', 'tour', 'ranking', 'created_at')
        read_only_fields = ('id', 'created_at')


class FavouritePlayerSerializer(serializers.ModelSerializer):
    player_details = PlayerSerializer(source='player', read_only=True)

    class Meta:
        model = FavouritePlayer
        fields = ('id', 'player', 'player_details', 'added_at')
        read_only_fields = ('id', 'added_at')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
