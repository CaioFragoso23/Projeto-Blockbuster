from rest_framework import serializers
from .models import RatingChoices
from .models import Movie
from users.serializers import UserSerializer
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(allow_null=True, default=None)
    rating = serializers.ChoiceField(choices=RatingChoices.choices, default=RatingChoices.G)
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.CharField(read_only=True, source="user.email")

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True, source="movie.title")
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.CharField(read_only=True, source="user.email")
    buyed_at = serializers.DateTimeField(read_only=True)

