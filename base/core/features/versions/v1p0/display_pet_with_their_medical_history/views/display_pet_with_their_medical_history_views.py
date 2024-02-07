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

        message = 'medical_history_records'
        errors = {}
        status = 'ok'

        # Include the count in the response data
        response_data = {
            "medical_history_count": medical_history_count,
            "message": message,
            "data": data,
            
            "status": status,
            "errors": errors
        }

        # Return the response
        return Response(response_data)

