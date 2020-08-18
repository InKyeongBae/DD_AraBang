import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from review.models import *
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string

class User(AbstractUser):

    """ Custom User Model """
    avatar = models.ImageField(upload_to="avatars", blank=True)
    superhost = models.BooleanField(default=False)
    school = models.ForeignKey(
        "community.School", related_name="community", on_delete=models.CASCADE, null=True
    )
    point = models.IntegerField(default=1000, null=True)
    buylist = models.CharField(default='', null=True, max_length=10000)
    email_first = models.CharField(max_length=20, default="", blank=True)
    point = models.IntegerField(default=10, null=True)
    #이메일 인증 
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "Verify DDAraBang Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return
