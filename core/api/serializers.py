from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models import Advisor, Booking

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )
        user.name = validated_data["name"]
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = (
            "id",
            "name",
            "email",
            "password",
        )


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ("id", "name", "photo_url")


class BookingSerializer(serializers.ModelSerializer):
    advisor = AdvisorSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ("id", "time", "advisor")
