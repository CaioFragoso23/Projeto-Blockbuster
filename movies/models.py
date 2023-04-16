from django.db import models

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
    added_by = models.CharField(max_length=50, null=True)
# Create your models here.
