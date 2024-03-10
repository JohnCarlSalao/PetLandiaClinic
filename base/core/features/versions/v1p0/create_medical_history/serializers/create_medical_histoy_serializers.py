from rest_framework import serializers
from core.models import Parent, Pets, MedicalHistory
from base.utilities.formatter import CustomDateFormatField
from base.utilities.helpers import validate_past, validate_future


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ['id']

class CreateMedicalHistorySerializer(serializers.ModelSerializer):
    pet = serializers.CharField()
    last_vaccination_date = CustomDateFormatField(validators =[validate_past], required=False)
    last_deworming_date = CustomDateFormatField(validators =[validate_past], required=False)
    date_hospitalized = CustomDateFormatField(validators =[validate_past], required=False)
    followup_checkup_date = CustomDateFormatField(validators =[validate_future],required=False)
    def to_internal_value(self, data):
        if "last_vaccination_date" in data and data["last_vaccination_date"] == "":
            data["last_vaccination_date"] = None
        if "last_deworming_date" in data and data["last_deworming_date"] == "":
            data["last_deworming_date"] = None
        if "date_hospitalized" in data and data ["date_hospitalized"] == "":
            data["date_hospitalized"] = None 
        if "followup_checkup_date" in data and data ["followup_checkup_date"]:
            data["followup_checkup_date"] = None       
        return super().to_internal_value(data)
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
