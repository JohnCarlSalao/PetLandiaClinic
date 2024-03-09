from rest_framework.response import Response
from core.models import MedicalHistory, Pets
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers.serializers import DisplayMedicalHistoryWithIDSerializer
from rest_framework import generics
class DisplayMedicalHistoryWithPetID(generics.ListAPIView):
    serializer_class = DisplayMedicalHistoryWithIDSerializer
    queryset = MedicalHistory.objects.all()

    def get_object(self):
        pet_id = self.kwargs.get('pet_id')
        pet_instance = get_object_or_404(Pets, id=pet_id)
        return get_object_or_404(self.queryset, pet=pet_instance)

