from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from tweet.models import Tweet


@api_view(["GET", "PUT"])
def like_tweet(request, tweet_id):
    """
    "GET" request: returns the number of likes for the tweet with the given id.
    "PUT" request: updates the number of likes for the tweet with the given id.
        if the user has already liked the selected tweet, the like is removed.
        if the user has not yet liked the selected tweet, the like is added.
        each user can add a maximum of one like to each tweet.
    """
    if request.method == "PUT" and request.user.is_authenticated:
        try:
            username = request.user.username
            likes = Tweet.objects.get(id=tweet_id).likes
            if username in likes:
                likes.remove(username)
            else:
                likes.append(username)
            Tweet.objects.filter(id=tweet_id).update(likes=likes)
            return Response(data={"likes": "updated"}, status=status.HTTP_200_OK)
        except Tweet.DoesNotExist:
            return Response(
                data={"likes": "tweet not found"}, status=status.HTTP_404_NOT_FOUND
            )
    if request.method == "GET":
        try:
            tweet = Tweet.objects.get(id=tweet_id).likes
            likes = len(tweet)
            return Response(data={"likes": likes}, status=status.HTTP_200_OK)
        except Tweet.DoesNotExist:
            return Response(
                data={"likes": "tweet not found"}, status=status.HTTP_404_NOT_FOUND
            )
