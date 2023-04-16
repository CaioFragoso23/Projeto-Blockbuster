from django.db import models
from users.models import User
class RatingChoices(models.TextChoices):
    G = ("G", "G")
    PG = ("PG", "PG")
    PG13 = ("PG-13", "PG-13")
    R = ("R", "R")
    NC17 = ("NC-17", "NC-17")

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(max_length=20, choices=RatingChoices.choices, default=RatingChoices.G)
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
        # null=True
    )

class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
# Create your models here.
