from rest_framework import serializers
from core.models import Parent, Pets, MedicalHistory
from base.utilities.formatter import CustomDateFormatField
from base.utilities.helpers import validate_past, validate_future
import datetime
class NullableFloatField(serializers.FloatField):
    def to_internal_value(self, value):
        if value == "":
            return None
        return super().to_internal_value(value)
class CreateMedicalHistoryWithIDSerializer(serializers.ModelSerializer):
    pet = serializers.CharField(read_only=True)
    last_vaccination_date = CustomDateFormatField(required=False, allow_null = True,  validators=[validate_past])
    last_deworming_date = CustomDateFormatField(required=False, allow_null = True, validators=[validate_past])
    date_hospitalized = CustomDateFormatField(required=False,allow_null = True,  validators=[validate_past])
    followup_checkup_date = CustomDateFormatField(required=False, allow_null = True, validators=[validate_future])
    initial_temp = NullableFloatField(required=False,)
    weight = NullableFloatField(required=False, )
    
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

