from authentication.managers import TwitterUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4


class TwitterUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name="UUID")
    email = models.EmailField(unique=True, max_length=254, verbose_name='Email address')
    name = models.CharField(max_length=50, verbose_name="Profile Name")
    bio = models.CharField(max_length=160, blank=True, verbose_name="Bio")
    website = models.CharField(max_length=100, blank=True, verbose_name="Website")
    location = models.CharField(max_length=30, blank=True, verbose_name="Location")
    birth_date = models.DateField(null=True, verbose_name="Birth Date")
    public = models.BooleanField(default=True, help_text="Indicates whether the profile is public", verbose_name="Public")
    following = models.IntegerField(default=0, help_text="Indicates the number of profiles following", verbose_name="Following")
    followers = models.IntegerField(default=0, help_text="Indicates the number of followers", verbose_name="Followers")

    REQUIRED_FIELDS = []

    objects = TwitterUserManager()

    def __str__(self):
        return self.username
