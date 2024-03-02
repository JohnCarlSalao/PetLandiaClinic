from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Pets, MedicalHistory, Parent
from base.utilities.generate_uid import generate_uuid
from base.utilities.constant import *
from ..serializers.create_medical_histoy_serializers import CreateMedicalHistorySerializer, PetsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiExample


class CreateMedicalHistoryViews(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    @extend_schema(request = CreateMedicalHistorySerializer,
                   responses={ok: CreateMedicalHistorySerializer},
                   description = 'To Create Medical History',
                   summary = 'Create medical history.', 
                   examples=[OpenApiExample(
            name='Create Medical History',
            value={
  "pet": "<pet_id>",
  "chief_complaint": "Nabarel sa paa",
  "medication_given_prior_to_check_up": "Antibiotics",
  "last_vaccination_given": "Anti-rabies",
  "last_vaccination_date": "2023/12/15",
  "last_vaccination_brand": "Pfizer",
  "last_deworming_brand": "DewormerX",
  "last_deworming_date": "2024/01/30",
  "last_deworming_given": "Tablet",
  "is_transferred_from_other_clinic": True,
  "name_of_clinic": "VetCare Clinic",
  "case": "Dog presented with limping on hind leg after running in the park.",
  "date_hospitalized": "2024/02/24",
  "diet": "High protein diet",
  "weight": 18,
  "initial_temp": 39.2,
  "heart_rate": "90 bpm",
  "respiratory_rate": "20 breaths per minute",
  "abnormal_findings": "Mild swelling on the affected paw",
  "is_cbc": True,
  "is_skin_scrape": True,
  "is_xray": True,
  "is_dfs": True,
  "is_urinalysis": True,
  "is_vaginal_smear": False,
  "tentative_diagnosis": "Soft tissue injury",
  "prognosis": "Good with proper rest and medication",
  "treatment_given": "Painkillers, anti-inflammatory drugs, and rest advised.",
  "take_home_meds": "Painkillers (Dosage: Twice daily after meals), Anti-inflammatory (Dosage: Once daily after meals)",
  "recommendations": "Strict rest for 1 week, avoid strenuous activity.",
  "followup_checkup_date": "2024/03/10"
}

        )],
                   
                
    
    )
    def post(self, request):
        serializer = CreateMedicalHistorySerializer(data=request.data)
        data = {}
        errors = {}
        status = None
        message = None

        if serializer.is_valid():
            pet_id = request.data.get('pet')

            try:
                pet_instance = Pets.objects.get(id=pet_id)
            except Pets.DoesNotExist:
                errors['pet'] = ['Invalid Pet ID']
                status = bad_request
                return Response({"status": status, "errors": errors}, status)

            medical_history_data = serializer.validated_data
            medical_history_data['pet'] = pet_instance
            pet_details = {
            'id': pet_instance.id,
            'name': pet_instance.name,
            'species': pet_instance.species,
            'breed': pet_instance.breed,
            'age': pet_instance.birthday,
            'color_or_markings': pet_instance.color_or_markings
            
        }
            
            uid = generate_uuid()
            medical_history_data['history_id'] = uid
            medical_history = MedicalHistory.objects.create(**medical_history_data)

            
            
            data = {
            'medical_history_id': medical_history.history_id,
            'pet': pet_details,
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
            status = created
            message = 'Successfully Created'
        else:
            errors = serializer.errors
            status = bad_request
        return Response({"message": message, "data": data, "status": status, "errors": errors}, status)