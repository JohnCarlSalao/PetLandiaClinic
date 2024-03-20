from rest_framework.views import APIView
from core.models import Pets, MedicalHistory, Parent 
from base.utilities.constant import *
from base.utilities.generate_uid import generate_uuid
from ..serializers.create_medical_history_views_with_id_serializers import CreateMedicalHistoryWithIDSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class CreateMedicalHistoryWithPetID(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, pet_id):
        serializer = CreateMedicalHistoryWithIDSerializer(data=request.data)
        
        if serializer.is_valid():
            pet_instance = get_object_or_404(Pets, id=pet_id)
            # Assuming parent_full_name is provided in the request data
            parent_full_name = request.data.get('parent', None)
            if not pet_instance:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "errors": {"pet": ["Invalid Pet ID"]}}, status=status.HTTP_400_BAD_REQUEST)
            if not parent_full_name:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "errors": {"parent_full_name": ["Parent full name is required"]}}, status=status.HTTP_400_BAD_REQUEST)
            
            # Fetch parent instance based on provided full name
            try:
                parent_instance = Parent.objects.get(full_name=parent_full_name)
            except Parent.DoesNotExist:
                return Response({"status": status.HTTP_400_BAD_REQUEST, "errors": {"parent_full_name": ["Parent with the provided full name does not exist"]}}, status=status.HTTP_400_BAD_REQUEST)

            medical_history_data = serializer.validated_data
            medical_history_data['pet'] = pet_instance
            medical_history_data['history_id'] = generate_uuid()
            medical_history_data['parent'] = parent_instance
            medical_history = MedicalHistory.objects.create(**medical_history_data)

            data = {
                'medical_history_id': medical_history.history_id,
                'pet_id': pet_instance.id,
                'name': pet_instance.name,
                'species': pet_instance.species,
                'parent': parent_instance.full_name,
                    
    
                'breed': pet_instance.breed,
                'birthday': pet_instance.birthday,
                'color_or_markings': pet_instance.color_or_markings,      
                'chief_complaint': medical_history.chief_complaint,
                'medication_given_prior_to_check_up': medical_history.medication_given_prior_to_check_up,
                'last_vaccination_given': medical_history.last_vaccination_given,
                'last_vaccination_date': medical_history.last_vaccination_date,
                'last_vaccination_brand': medical_history.last_vaccination_brand,
                'last_deworming_brand': medical_history.last_deworming_brand,
                'last_deworming_date': medical_history.last_deworming_date,
                'last_deworming_given': medical_history.last_deworming_given,
                'is_transferred_from_other_clinic': medical_history.is_transferred_from_other_clinic,
                'name_of_clinic': medical_history.name_of_clinic,
                'case': medical_history.case,
                'date_hospitalized': medical_history.date_hospitalized,
                'diet': medical_history.diet,
                'weight': medical_history.weight,
                'initial_temp': medical_history.initial_temp,
                'heart_rate': medical_history.heart_rate,
                'respiratory_rate': medical_history.respiratory_rate,
                'abnormal_findings': medical_history.abnormal_findings,
                'is_cbc': medical_history.is_cbc,
                'is_skin_scrape': medical_history.is_skin_scrape,
                'is_xray': medical_history.is_xray,
                'is_dfs': medical_history.is_dfs,
                'is_urinalysis': medical_history.is_urinalysis,
                'is_vaginal_smear': medical_history.is_vaginal_smear,
                'tentative_diagnosis': medical_history.tentative_diagnosis,
                'prognosis': medical_history.prognosis,
                'treatment_given': medical_history.treatment_given,
                'take_home_meds': medical_history.take_home_meds,
                'recommendations': medical_history.recommendations,
                'followup_checkup_date': medical_history.followup_checkup_date
                
            }
            
            return Response({"message": "Successfully Created", "data": data, "status": status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Validation Error", "errors": serializer.errors, "status": status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

# class CreateMedicalHistoryWithPetID(generics.CreateAPIView):
#     queryset = MedicalHistory.objects.all()
#     serializer_class = CreateMedicalHistoryWithIDSerializer

#     def post(self, request, pet_id):
#         # Get the pet instance or return 404 if not found
#         pet_instance = get_object_or_404(Pets, id=pet_id)

#         serializer = self.get_serializer(data=request.data)
#         request.data['history_id'] = generate_uuid()

#         # Initialize serializer with request data
#         serializer = self.serializer_class(data=request.data)

#         # Validate serializer data
#         if serializer.is_valid():
#             serializer.save(pet=pet_instance)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)