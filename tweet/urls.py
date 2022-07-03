from django.urls import path, include
from rest_framework import routers
from tweet.views import TweetsAPI

router = routers.DefaultRouter()
router.register('tweets', TweetsAPI)

urlpatterns = [
    path('', include(router.urls)),
]
