from rest_framework import serializers
from core.models import CustomUser


class ViewProfileSerializer(serializers.ModelSerializer):
     class Meta:
        model = CustomUser
        fields = [ 'name', 'username', 'email']