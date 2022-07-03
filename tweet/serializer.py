from rest_framework.serializers import HyperlinkedModelSerializer
from tweet.models import Tweet

class TweetSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
