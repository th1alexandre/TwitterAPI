from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from tweet.serializer import TweetSerializer
from tweet.models import Tweet
from django.db.models import Q


class TweetsAPI(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class RecentFeedAPI(ModelViewSet):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()

    def get_queryset(self):
        user = self.request.user.username
        return Tweet.objects.filter(~Q(author=user)).order_by("-created_at")[:10]
