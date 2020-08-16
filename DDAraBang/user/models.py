from django.db import models
from django.contrib.auth.models import AbstractUser
from review.models import *


class User(AbstractUser):

    """ Custom User Model """
    avatar = models.ImageField(upload_to="avatars", blank=True)
    superhost = models.BooleanField(default=False)
    school = models.ForeignKey(
        "community.School", related_name="community", on_delete=models.CASCADE, null=True
    )
    point = models.IntegerField(default=1000, null=True)
    buylist = models.CharField(default='', null=True, max_length=10000)