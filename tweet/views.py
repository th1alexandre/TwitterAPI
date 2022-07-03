from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from tweet.serializer import TweetSerializer
from tweet.models import Tweet

class TweetsAPI(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
