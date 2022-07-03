from django.urls import path, include
from rest_framework import routers
from tweet.views import TweetsAPI, RecentFeedAPI

router = routers.DefaultRouter()
router.register("tweets", TweetsAPI)
router.register("feed", RecentFeedAPI)

urlpatterns = [
    path("", include(router.urls)),
]
