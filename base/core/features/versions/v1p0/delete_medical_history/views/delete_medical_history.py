from rest_framework.response import Response
from rest_framework.views import APIView
from base.utilities.constant import *
from core.models import MedicalHistory
from django.http import Http404


class DeleteMedicalRecordsViews(APIView):

    
    def get_medical_records(self, pk):
        try: 
            return MedicalHistory.objects.get (pk=pk)
        except MedicalHistory.DoesNotExist:
            raise Http404
    def delete(self, request,pk):
        
        errors = {}
        data = {}
        status = None
        pets = self.get_medical_records(pk)
        pets.delete()
        message = 'Successfully Deleted'
        status = no_content        
        return Response ({"Message": message, "data": data, "status": status, "errors": errors })
    