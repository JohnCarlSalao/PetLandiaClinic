from rest_framework.response import Response
from rest_framework.views import APIView
from base.utilities.constant import *
from core.models import Pets
from django.http import Http404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
class DeletePetsViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_pet(self, pk):
        try: 
            return Pets.objects.get (pk=pk)
        except Pets.DoesNotExist:
            raise Http404
    @extend_schema(
                   description = 'To delete pets',
                   summary = 'Delete Pets.'
            
    )
    def delete(self, request,pk):
        
        errors = {}
        data = {}
        status = None
        pets = self.get_pet(pk)
        pets.delete()
        message = 'Successfully Deleted'
        status = no_content        
        return Response ({"Message": message, "data": data, "status": status, "errors": errors },status)
    
    