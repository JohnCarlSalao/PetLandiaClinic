from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Parent, MedicalHistory, Pets
from ..serializers.display_pet_with_their_medical_history_serializers import DisplayMedicalHistoryPetSerializer, PetsSerializer
from base.utilities.constant import *
from django.http import Http404
from django.shortcuts import get_object_or_404






class MedicalHistoryByPetIDView(APIView):
    def get(self, request, pet_id):
        # Fetch the pet instance using the provided pet_id
        pet_instance = get_object_or_404(Pets, id=pet_id)

        # Fetch all medical history records associated with the pet
        medical_history_records = MedicalHistory.objects.filter(pet=pet_instance)

        # Get the count of medical history records
        medical_history_count = medical_history_records.count()

        # Serialize the data using the DisplayMedicalHistoryPetSerializer
        serializer = DisplayMedicalHistoryPetSerializer(medical_history_records, many=True)
        
        # Get the serialized data
        data = serializer.data
        
        # Fetch parent(s) associated with the pet
        parents_info = []
        for parent in pet_instance.parent_set.all():
            parent_info = {
                'parent_id': parent.id,
                'first_name': parent.first_name,
                'last_name': parent.last_name,
                'occupation': parent.occupation,
                'contact_number': parent.contact_number,
            }
            parents_info.append(parent_info)

        message = 'medical_history_records'
        errors = {}
        status = ok

        response_data = {
            "message": message,
            "data": {
                'owner_info': parents_info,
                'medical_history_count': medical_history_count,
                'medical_history_records': data,
            },
            "status": status,
            "errors": errors
        }

        # Return the response
        return Response(response_data)

