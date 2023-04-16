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
    added_by = serializers.CharField(allow_null=True, default=None)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
