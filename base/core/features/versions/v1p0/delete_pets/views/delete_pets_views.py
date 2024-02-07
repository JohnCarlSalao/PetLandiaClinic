from rest_framework.response import Response
from rest_framework.views import APIView
from base.utilities.constant import *
from core.models import Pets
from django.http import Http404


class DeletePetsViews(APIView):

    
    def get_pet(self, pk):
        try: 
            return Pets.objects.get (pk=pk)
        except Pets.DoesNotExist:
            raise Http404
    def delete(self, request,pk):
        
        errors = {}
        data = {}
        status = None
        pets = self.get_pet(pk)
        pets.delete()
        message = 'Successfully Deleted'
        status = no_content        
        return Response ({"Message": message, "data": data, "status": status, "errors": errors })
    
    