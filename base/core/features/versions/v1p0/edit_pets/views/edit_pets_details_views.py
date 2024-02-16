from rest_framework.views import APIView
from rest_framework.response import Response 
from core.models import Pets
from ..serializers.edit_pets_serializers import EditPetsSerializers
from base.utilities.constant import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


from django.http import Http404

class EditPetsDetailsViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_pet(self, pk):
        try: 
            return Pets.objects.get (pk=pk)
        except Pets.DoesNotExist:
            raise Http404
        
    def put (self, request, pk):
        data = {}
        errors = {}
        status = None 
        message =None 
        pet= self.get_pet(pk)
        serializer =EditPetsSerializers (pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data =serializer.data
            message = 'Successfully Updated'
            status = ok
        else:
            data = serializer.data
            message = 'Error'
            status = bad_request
            errors = serializer.errors
        return Response({"message": message, "data": data, "status": status, "errors": errors})
    
