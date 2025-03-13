from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser

CustomUser = get_user_model()


class CustomSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ["id", "full_name", "email"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
