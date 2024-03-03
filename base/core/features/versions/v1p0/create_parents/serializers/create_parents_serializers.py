from rest_framework import serializers
from core.models import Parent
from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
@extend_schema_serializer(
    examples = [
         OpenApiExample(
            'Simple Example',
            summary='short summary',
            description='longer description',
            value={
                'full_name': 'Ranxer Balondo',
                'occupation': 'Ceo',  
                'contact_number':'09292811165'
            },
            request_only=True, # signal that example only applies to requests
            response_only=True, # signal that example only applies to responses
        ),
    ]
)
class CreateParentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['full_name', 'occupation', 'contact_number']
