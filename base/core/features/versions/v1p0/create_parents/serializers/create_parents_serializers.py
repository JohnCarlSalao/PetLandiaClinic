from rest_framework import serializers
from core.models import Parent

class CreateParentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'occupation', 'contact_number']
        