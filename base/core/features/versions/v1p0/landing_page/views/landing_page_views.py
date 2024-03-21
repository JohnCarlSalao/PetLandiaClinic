from rest_framework.views import APIView 
from rest_framework.response import Response 
from base.utilities.constant import *
from core.models import Pets, Parent, MedicalHistory
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema
from datetime import date
class LandingPageView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @extend_schema(
                    summary = 'List all the item in dashboard',
                    
                   description = 'To get the count on Dashboard/ Landing Page.',
                   
            
    )
    def get(self, request):
        today = datetime.now().date()
        today_date = date.today()
        current_year = datetime.now().year
        current_month = datetime.now().month
        yesterday = today - timedelta(days=1)
        total_pets = Pets.objects.count()
        total_parents = Parent.objects.count()
        total_medical_records = MedicalHistory.objects.count()
        total_medical_records_for_the_month = MedicalHistory.objects.filter(followup_checkup_date__month=current_month).count()
        total_medical_records_for_the_year = MedicalHistory.objects.filter(followup_checkup_date__year=current_year).count()
        today_or_upcoming_checkups = MedicalHistory.objects.filter(followup_checkup_date__gte=today).count()        
        yesterday_checkups = MedicalHistory.objects.filter(followup_checkup_date=yesterday).count()
        today_checkups = MedicalHistory.objects.filter(followup_checkup_date=today).count()
        # today Checkups need followup to be fix soon
        
       
        data = {
            'total_pets': total_pets,
            'total_parents': total_parents,
            'total_medical_records': total_medical_records,
            'today_or_upcoming_checkups': today_or_upcoming_checkups,
            'yesterday_checkups': yesterday_checkups,
            'today_checkups': today_checkups,
            'total_medical_records_for_the_month':total_medical_records_for_the_month,
            'total_medical_records_for_the_year':  total_medical_records_for_the_year,
        }

        status = ok 
        message = 'Successful'
        errors ={}
        return Response({"message":message, "data": data, "status": status, "errors": errors},status)