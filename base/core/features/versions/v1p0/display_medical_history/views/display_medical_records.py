from rest_framework.views import APIView
from core.models import Parent, MedicalHistory
from base.utilities.constant import *
from rest_framework.response import Response
from ..serializers.display_medical_records_serializers import DisplayMedicalHistorySerializer
from django.http import Http404
import pytz


class DisplayMedicalRecordsViews(APIView):
    def get(self, request):
        medical_history = MedicalHistory.objects.all().values('history_id',
            'pet', 'chief_complaint', 'medication_given_prior_to_check_up',
            'last_vaccination_given', 'last_vaccination_date', 'last_vaccination_brand',
            'last_deworming_brand', 'last_deworming_date', 'last_deworming_given',
            'is_transferred_from_other_clinic', 'name_of_clinic', 'case',
            'date_hospitalized', 'diet', 'weight', 'initial_temp', 
            'heart_rate', 'respiratory_rate', 'abnormal_findings', 'is_cbc', 'is_skin_scrape',
            'is_xray', 'is_dfs', 'is_urinalysis', 'is_vaginal_smear',
            'tentative_diagnosis', 'prognosis', 'treatment_given', 'take_home_meds',
            'recommendations', 'followup_checkup_date')
        data = {'medical_history':list(medical_history)}
        message = 'Success'
        status = ok
        return Response({"Message": message, "data": data, "status": status})

class DisplayMedicalRecordsIndivViews(APIView):
    def get_medical_records(self, pk):
        try: 
            return MedicalHistory.objects.get(pk=pk)
        except MedicalHistory.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        
        parent = self.get_medical_records(pk)
        serializer = DisplayMedicalHistorySerializer(parent)
        data =serializer.data
        status = ok
        message = 'Results'
        errors = {}
        return Response({"message": message, "data": data, "status": status, "errors": errors})
