from rest_framework.viewsets import ModelViewSet
from tweet.serializer import TweetSerializer
from tweet.models import Tweet

class TweetsAPI(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
