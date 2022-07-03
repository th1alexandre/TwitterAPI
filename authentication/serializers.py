from rest_framework.serializers import ModelSerializer
from authentication.models import TwitterUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = TwitterUser
        fields = (
            "username",
            "email",
            "name",
            "bio",
            "website",
            "location",
            "birth_date",
            "public",
            "following",
            "followers",
        )


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = TwitterUser
        fields = (
            "username",
            "password",
            "email",
            "name",
            "bio",
            "website",
            "location",
            "birth_date",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = TwitterUser.objects.create_user(**validated_data)
        return user
