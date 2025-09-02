from rest_framework import serializers
from APIs.models import Profile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        # fields='__all__'
        exclude = ["id"]