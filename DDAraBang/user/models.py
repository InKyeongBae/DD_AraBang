<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """ Custom User Model """
    avatar = models.ImageField(upload_to="avatars", blank=True)
    superhost = models.BooleanField(default=False)
    school = models.ForeignKey(
        "community.School", related_name="community", on_delete=models.CASCADE, null=True
    )
    point = models.IntegerField(null=True)
=======
>>>>>>> yurim
