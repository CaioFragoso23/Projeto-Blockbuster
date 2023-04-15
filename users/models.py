from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    email = models.CharField(max_length=127, default="email", unique=True)
    first_name = models.CharField(max_length=50, default="first_name")
    last_name = models.CharField(max_length=50, default="last_name")
    birthdate = models.DateField(null=True)
    is_employee = models.BooleanField(null=True, default=False)
# Create your models here.
