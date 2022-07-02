from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import TwitterUser


class TwitterUserAdmin(UserAdmin):
    model = TwitterUser
    list_display = ["id", "username", "email"]
    list_display_links = ["id"]
    list_per_page = 10


admin.site.register(TwitterUser, TwitterUserAdmin)
