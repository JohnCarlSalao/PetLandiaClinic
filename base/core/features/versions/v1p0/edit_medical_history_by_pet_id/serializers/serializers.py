from rest_framework import serializers
from core.models import MedicalHistory
from base.utilities.formatter import CustomDateFormatField
from base.utilities.helpers import validate_past, validate_future
from core.features.versions.v1p0.display_pets.serializers.display_serializers import DisplayPetSerializer

class DisplayMedicalHistoryWithIDSerializer(serializers.ModelSerializer):
    pet = DisplayPetSerializer(read_only = True)
    last_vaccination_date = CustomDateFormatField(validators =[validate_past], required=False)
    last_deworming_date = CustomDateFormatField(validators =[validate_past], required=False)
    date_hospitalized = CustomDateFormatField(validators =[validate_past], required=False)
    followup_checkup_date = CustomDateFormatField(validators =[validate_future],required=False)
    class Meta:
        model = MedicalHistory
        fields = [
            'pet', 'chief_complaint', 'medication_given_prior_to_check_up',
            'last_vaccination_given', 'last_vaccination_date', 'last_vaccination_brand',
            'last_deworming_brand', 'last_deworming_date', 'last_deworming_given',
            'is_transferred_from_other_clinic', 'name_of_clinic', 'case',
            'date_hospitalized', 'diet', 'weight', 'initial_temp',  
            'heart_rate', 'respiratory_rate', 'abnormal_findings', 'is_cbc', 'is_skin_scrape',
            'is_xray', 'is_dfs', 'is_urinalysis', 'is_vaginal_smear',
            'tentative_diagnosis', 'prognosis', 'treatment_given', 'take_home_meds',
            'recommendations', 'followup_checkup_date'
        ]

