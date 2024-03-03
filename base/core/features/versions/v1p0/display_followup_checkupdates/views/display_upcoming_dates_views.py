from core.models import Parent, MedicalHistory, Pets
from base.utilities.constant import *
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date
from ..serializer.display_upcoming_dates_serializers import DisplayMedicalHistorySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

class DisplayUpcomingFollowupCheckUpDatesViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @extend_schema(
                   description = 'To Display upcoming dates of followup checkup dates of pet.',
                   summary = 'Display Upcoming Checkups'
            
    )
    def get(self, request):
        today = date.today()
        upcoming_checkups = MedicalHistory.objects.filter(followup_checkup_date__gte=today).order_by('followup_checkup_date')
        
        data = []
        for checkup in upcoming_checkups:
            pet = checkup.pet
            owner = pet.parent_set.first()  
            data.append({
                'history_id': checkup.history_id,
                'pet_id': pet.id,
                'pet_name': pet.name,
                'pet_breed':pet.breed,
                'owner_name': f"{owner.full_name}" if owner else "Unknown Owner",
                'phone_number': owner.contact_number if owner else "Unknown number",
                'followup_checkup_date': checkup.followup_checkup_date,
                
            })
        
        message = 'Results'
        status = ok
        errors = {}
        return Response({"message": message, "data": data, "status": status, "errors": errors},status)