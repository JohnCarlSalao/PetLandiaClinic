from rest_framework import serializers
from core.models import Parent, Pets
class DisplayParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    number_of_pets = serializers.SerializerMethodField()
    class Meta:
        model = Parent
        fields = ['id', 'first_name', 'last_name', 'occupation', 'contact_number','number_of_pets', 'pets', ]
        depth = 1  # Specify the depth to serialize related objects
        
    def get_number_of_pets(self, obj):
        return obj.pets.count()

class PetsSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(format="%m-%d-%Y")
    created = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S.%f")
    class Meta:
        model = Pets
        fields = ['id', 'name', 'species', 'breed', 'color_or_markings', 'birthday', 'sex']

    def to_representation(self, instance):
        # Override to_representation to remove 'sex' field if it's not needed
        representation = super().to_representation(instance)
        if self.context.get('exclude_sex'):
            representation.pop('sex')
        return representation
    