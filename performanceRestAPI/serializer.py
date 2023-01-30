from rest_framework import serializers
from .models import Artist
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'artist_id', 'artist', 'title', 'date', 'date_full', 'link', 'performance_info')

class ArtistSerilalizer(serializers.ModelSerializer):
    artist = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'artist')