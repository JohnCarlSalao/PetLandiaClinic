from rest_framework import serializers
from core.models import MedicalHistory
from core.features.versions.v1p0.display_pets.serializers.display_serializers import DisplayPetSerializer
from base.utilities.formatter import CustomDateFormatField, NullableFloatField
from core.models import Parent
from core.features.versions.v1p0.create_medical_history_with_pet_id_as_parameter.serializers.create_medical_history_views_with_id_serializers import NullableDateField
from base.utilities.helpers import validate_future, validate_past
class EditMedicalRecordSerializers(serializers.ModelSerializer):
    last_vaccination_date = NullableDateField(input_formats=['%Y/%m/%d'] ,  required = False)
    followup_checkup_date = NullableDateField(input_formats=['%Y/%m/%d'],   required = False)
    last_deworming_date = NullableDateField(input_formats=['%Y/%m/%d'] , required = False )
    date_hospitalized = NullableDateField(input_formats=['%Y/%m/%d'],  required = False)
    initial_temp = NullableFloatField(required=False,)
    weight = NullableFloatField(required=False, )
    pet = DisplayPetSerializer(read_only = True)
    parent = serializers.SlugRelatedField(slug_field='full_name', queryset = Parent.objects.all())
    class Meta:
        model =MedicalHistory
        fields = ['chief_complaint', 'medication_given_prior_to_check_up',
                  'parent','pet',
            'last_vaccination_given', 'last_vaccination_date', 'last_vaccination_brand',
            'last_deworming_brand', 'last_deworming_date', 'last_deworming_given',
            'is_transferred_from_other_clinic', 'name_of_clinic', 'case',
            'date_hospitalized', 'diet', 'weight', 'initial_temp', 
            'heart_rate', 'respiratory_rate', 'abnormal_findings', 'is_cbc', 'is_skin_scrape',
            'is_xray', 'is_dfs', 'is_urinalysis', 'is_vaginal_smear',
            'tentative_diagnosis', 'prognosis', 'treatment_given', 'take_home_meds',
            'recommendations', 'followup_checkup_date']

