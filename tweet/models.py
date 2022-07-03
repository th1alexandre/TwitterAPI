from authentication.models import TwitterUser
from django.db import models
from uuid import uuid4


class Tweet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name="UUID")
    author = models.ForeignKey(TwitterUser, to_field="username", on_delete=models.CASCADE, help_text="The author of the tweet", verbose_name="Author")
    content = models.CharField(max_length=280, null=False, blank=False, help_text="The content of the tweet", verbose_name="Content")
    public = models.BooleanField(default=True, help_text="Defines whether the tweet is public", verbose_name="Public") # Todo: add reference to the TwitterUser 'public' field. Currently default=True
    likes = models.IntegerField(default=0, help_text="The number of likes", verbose_name="Likes")
    retweets = models.IntegerField(default=0, help_text="The number of retweets", verbose_name="Retweets")
    commented_retweets = models.IntegerField(default=0, help_text="The number of commented retweets", verbose_name="Commented Retweets")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time the tweet was created", verbose_name="Created At")

    def __str__(self):
        return f"Tweet id: {self.id}"
