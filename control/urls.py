from django.urls import path
from control.views import like_tweet

urlpatterns = [
    path('like/<uuid:tweet_id>/', like_tweet, name='like_tweet'),
]
