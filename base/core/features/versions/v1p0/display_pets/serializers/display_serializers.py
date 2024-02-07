from rest_framework import serializers
from core.models import Pets
class DisplayPetSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(format="%m-%d-%Y")
    created = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S.%fZ")
    modified = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S.%fZ")
    class Meta:
        model = Pets
        fields = '__all__'

        