from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import MedicalHistory
from ..serializers.edit_medical_record_serializers import EditMedicalRecordSerializers
from base.utilities.constant import *
from django.http import Http404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import generics
class EditMedicalRecordViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    

    def get_parent(self, pk):
        try:
            return MedicalHistory.objects.get(pk=pk)
        except MedicalHistory.DoesNotExist:
            raise Http404
    @extend_schema(request = EditMedicalRecordSerializers,
                   responses={ok: EditMedicalRecordSerializers},
                   description = 'To edit medical history.',
                   summary = 'Editing medical history via id.',
                   examples=[OpenApiExample(
            name='Create Medical History',
            value={
  "pet": "<pet_id>",
  "parent": "parent full name",
  "chief_complaint": "Nabarel sa paa",
  "medication_given_prior_to_check_up": "None",
  "last_vaccination_given": "Canine distemper",
  "last_vaccination_date": "2023/11/20",
  "last_vaccination_brand": "Merck",
  "last_deworming_brand": "WormGuard",
  "last_deworming_date": "2024/01/15",
  "last_deworming_given": "Liquid",
  "is_transferred_from_other_clinic": False,
  "name_of_clinic": "",
  "case": "Cat found with a slight limp on one hind leg.",
  "date_hospitalized": "2024/02/24",
  "diet": "Regular cat food",
  "weight": 6.5,
  "initial_temp": 38.7,
  "heart_rate": "100 bpm",
  "respiratory_rate": "24 breaths per minute",
  "abnormal_findings": "Tenderness on palpation of the affected limb",
  "is_cbc": False,
  "is_skin_scrape": True,
  "is_xray": False,
  "is_dfs": False,
  "is_urinalysis": True,
  "is_vaginal_smear": False,
  "tentative_diagnosis": "Muscle strain",
  "prognosis": "Excellent with rest and observation",
  "treatment_given": "Rest advised, no medication prescribed.",
  "take_home_meds": "",
  "recommendations": "Monitor for any worsening of symptoms.",
   "followup_checkup_date": "2024/03/03"
}
)],)
    def put(self, request, pk):
        data = {}
        errors = {}
        status = None
        medical_history = self.get_parent(pk)
        data = request.data.copy()
        data.setdefault('chief_complaint', medical_history.chief_complaint)
        data.setdefault('medication_given_prior_to_check_up', medical_history.medication_given_prior_to_check_up)
        data.setdefault('last_vaccination_given', medical_history.last_vaccination_given)
        data.setdefault('last_vaccination_date', medical_history.last_vaccination_date)
        data.setdefault('last_vaccination_brand', medical_history.last_vaccination_brand)
        data.setdefault('last_deworming_brand', medical_history.last_deworming_brand)
        data.setdefault('last_deworming_date', medical_history.last_deworming_date)
        data.setdefault('last_deworming_given', medical_history.last_deworming_given)
        data.setdefault('is_transferred_from_other_clinic', medical_history.is_transferred_from_other_clinic)
        data.setdefault('name_of_clinic', medical_history.name_of_clinic)
        data.setdefault('case', medical_history.case)
        data.setdefault('date_hospitalized', medical_history.date_hospitalized)
        data.setdefault('diet', medical_history.diet)
        data.setdefault('weight', medical_history.weight)
        data.setdefault('initial_temp', medical_history.initial_temp)
        data.setdefault('heart_rate', medical_history.heart_rate)
        data.setdefault('respiratory_rate', medical_history.respiratory_rate)
        data.setdefault('abnormal_findings', medical_history.abnormal_findings)
        data.setdefault('is_cbc', medical_history.is_cbc)
        data.setdefault('is_skin_scrape', medical_history.is_skin_scrape)
        data.setdefault('is_xray', medical_history.is_xray)
        data.setdefault('is_dfs', medical_history.is_dfs)
        data.setdefault('is_urinalysis', medical_history.is_urinalysis)
        data.setdefault('is_vaginal_smear', medical_history.is_vaginal_smear)
        data.setdefault('tentative_diagnosis', medical_history.tentative_diagnosis)
        data.setdefault('prognosis', medical_history.prognosis)
        data.setdefault('treatment_given', medical_history.treatment_given)
        data.setdefault('take_home_meds', medical_history.take_home_meds)
        data.setdefault('recommendations', medical_history.recommendations)
        data.setdefault('followup_checkup_date', medical_history.followup_checkup_date)
        serializer = EditMedicalRecordSerializers(medical_history, data=data, partial=True)
        

        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            data = serializer.data
            status = ok
            errors = serializer.errors
            return Response({"message": 'Successfully Updated', "data": data, "status": status},status)
        else:
            status = bad_request
            data = serializer.data
            errors = serializer.errors
            return Response({"message": 'Error', "data": data, "status": status, "errors": errors},status)
        
    class EditMedicalRecordsViewsV2(generics.RetrieveUpdateAPIView):
        serializer_class = EditMedicalRecordSerializers
        queryset = MedicalHistory.objects.all()

        def get_serializer_class(self):
            if self.request.method == "PUT":
                return EditMedicalRecordSerializers
            return super().get_serializer_class()

