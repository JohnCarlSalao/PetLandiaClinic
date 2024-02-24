from rest_framework.views import APIView 
from rest_framework.response import Response 
from base.utilities.constant import *
from core.models import Pets, Parent, MedicalHistory
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema
class LandingPageView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @extend_schema(
                   description = 'To get the count on Dashboard/ Landing Page.',
                   
            
    )
    def get(self, request):
        total_pets = Pets.objects.count()
        total_parents = Parent.objects.count()
        total_medical_records = MedicalHistory.objects.count()
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        today_or_upcoming_checkups = MedicalHistory.objects.filter(followup_checkup_date__gte=today).count()        
        yesterday_checkups = MedicalHistory.objects.filter(followup_checkup_date=yesterday).count()

       
        data = {
            'total_pets': total_pets,
            'total_parents': total_parents,
            'total_medical_records': total_medical_records,
            'today_or_upcoming_checkups': today_or_upcoming_checkups,
            'yesterday_checkups': yesterday_checkups
            
        }

        status = ok 
        message = 'Successful'
        errors ={}
        return Response({"message":message, "data": data, "status": status, "errors": errors})