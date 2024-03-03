from rest_framework import serializers
from core.models import Pets, Parent
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['id', 'full_name', 'occupation', 'contact_number']

class DisplayPetSerializer(serializers.ModelSerializer):
    
    birthday = serializers.DateField(format="%m-%d-%Y")
    created = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S%f")

    class Meta:
        model = Pets
        fields = ['id', 'name', 'species', 'breed', 'color_or_markings', 'birthday', 'sex', 'created',]

