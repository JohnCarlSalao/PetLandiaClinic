from rest_framework.views import APIView
from core.models import Parent, MedicalHistory, Pets
from base.utilities.constant import *
from rest_framework.response import Response
from ..serializers.display_medical_records_serializers import DisplayMedicalHistorySerializer
from django.http import Http404
import pytz
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
class DisplayMedicalRecordsViews(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @extend_schema(request = DisplayMedicalHistorySerializer,
                   responses={ok: DisplayMedicalHistorySerializer},
                   description = 'To Display medical records of the pet.',
                   summary = 'Display medical records.'
            
    )
    def get(self, request):
        medical_history = MedicalHistory.objects.all()
        serializer = DisplayMedicalHistorySerializer(medical_history, many=True)
        
       
        data = []
        for record in serializer.data:
            pet_id = record['pet']['id']
            owner_info = self.get_owner_info(pet_id)
            record['owner'] = owner_info
            data.append(record)
        
        message = 'Success'
        status = ok
        return Response({"message": message, "data": data, "status": status})
    
    def get_owner_info(self, pet_id):
        owner = None
        pet = Pets.objects.get(id=pet_id)
        owner = pet.parent_set.first()  
        owner_info = {
            'first_name': owner.first_name if owner else None,
            'last_name': owner.last_name if owner else None,
            'contact_number': owner.contact_number if owner else None
        }
        return owner_info





class DisplayMedicalRecordsIndivViews(APIView):
    def get_medical_record(self, pk):
        try: 
            return MedicalHistory.objects.get(pk=pk)
        except MedicalHistory.DoesNotExist:
            raise NotFound("Medical record not found")
    
    def get_owner_info(self, pet):
        owner_info = {}
        if pet:
            owner = pet.parent_set.first()  # Assuming one pet has only one owner
            if owner:
                owner_info = {
                    'owner_id':owner.id, 
                    'owner_first_name': owner.first_name,
                    'owner_last_name': owner.last_name,
                    'owner_contact_number':owner.contact_number
                    # Add more owner information if needed
                }
        return owner_info
    @extend_schema(request = DisplayMedicalHistorySerializer,
                   responses={ok: DisplayMedicalHistorySerializer},
                   description = 'To Display medical records of the pet individually.',
                   summary = 'Display medical records via ID.'
            
    )
    def get(self, request, pk):
        medical_record = self.get_medical_record(pk)
        serializer = DisplayMedicalHistorySerializer(medical_record)
        data = serializer.data

        # Fetch owner information
        owner_info = self.get_owner_info(medical_record.pet)
        data['owner'] = owner_info

        status = ok
        message = 'Success'
        errors = {}
        return Response({"message": message, "data": data, "status": status, "errors": errors})
