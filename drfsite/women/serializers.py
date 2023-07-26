import io

from rest_framework import serializers
from .models import LeatherClothes


class LeatherSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = LeatherClothes
        fields = "__all__"

