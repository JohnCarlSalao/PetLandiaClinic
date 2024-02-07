from rest_framework import serializers
from core.models import Parent
class DisplayParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'
        