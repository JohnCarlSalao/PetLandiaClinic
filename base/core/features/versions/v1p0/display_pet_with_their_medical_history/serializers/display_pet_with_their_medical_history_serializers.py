from rest_framework import serializers
from core.models import Parent, Pets, MedicalHistory

class PetsSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(format="%m-%d-%Y")
    created = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S.%fZ")
    modified = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S.%fZ")
    class Meta:
        model = Pets
        fields = '__all__'

class DisplayMedicalHistoryPetSerializer(serializers.ModelSerializer):
    pet = PetsSerializer()

    class Meta:
        model = MedicalHistory
        fields = ['history_id',
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

        