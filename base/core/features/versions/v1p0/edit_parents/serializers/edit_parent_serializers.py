from rest_framework import serializers
from core.models import Parent, Pets

class EditParentSerializer(serializers.ModelSerializer):
    pets = serializers.PrimaryKeyRelatedField(queryset=Pets.objects.all(), many=True)
    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'pets', 'occupation', 'contact_number']