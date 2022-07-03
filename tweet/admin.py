from django.contrib import admin
from tweet.models import Tweet

class Tweets(admin.ModelAdmin):
    list_display = ['id', 'author', 'public', 'likes', 'retweets', 'commented_retweets', 'created_at']
    list_display_links = ['id']
    list_per_page = 10
    search_fields = ['id','author__username', 'content']

admin.site.register(Tweet, Tweets)
