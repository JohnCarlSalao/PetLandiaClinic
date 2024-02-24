from rest_framework.views import APIView
from core.models import Pets
from base.utilities.constant import *
from rest_framework.response import Response
from ..serializers.display_serializers import DisplayPetSerializer
from django.http import Http404
import pytz
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

class DisplayPetViews(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    @extend_schema(request = DisplayPetSerializer,
                   responses={ok: DisplayPetSerializer},
                   description = 'To Display pets with owner',
                   summary = 'Display all Pets.'
            
    )
    
    def get(self, request):
        pets = Pets.objects.all().order_by('-created')
        serializer = DisplayPetSerializer(pets, many=True)
        data = serializer.data
        
        # Fetch owner information for each pet
        for pet in data:
            pet_obj = Pets.objects.get(id=pet['id'])
            owners_info = []
            for owner in pet_obj.parent_set.all():
                owner_info = {
                    'parent_id' : owner.id,
                    'first_name': owner.first_name,
                    'last_name': owner.last_name,
                    'occupation': owner.occupation,
                    'contact_number': owner.contact_number,
                }
                owners_info.append(owner_info)
            pet['parents'] = owners_info
         
        message = 'Success'
        status = ok
        return Response({"message": message, "data": data, "status": status})
    
class DisplayPetDetailViews(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get_pet(self, pk):
        try: 
            return Pets.objects.get(pk=pk)
        except Pets.DoesNotExist:
            return None
    @extend_schema(request = DisplayPetSerializer,
                   responses={ok: DisplayPetSerializer},
                   description = 'To Display pets details',
                   summary = 'Display Pets via id.'
            
    )
    def get(self, request, pk):
        pet = self.get_pet(pk)
        if pet is None:
            message = 'Pet does not exist'
            status = not_Found
            data = {}
            errors = {}
            return Response({"message": message, "data": data, "status": status, "errors": errors})
        parents_info = []
        for parent in pet.parent_set.all():
            parent_info = {
                'parent_id': parent.id,
                'first_name': parent.first_name,
                'last_name': parent.last_name,
                'occupation': parent.occupation,
                'contact_number': parent.contact_number,
            }
            parents_info.append(parent_info)
        serializer = DisplayPetSerializer(pet)
        pet_data = serializer.data
        pet_data['parents'] = parents_info
        message = 'Success'
        status = ok
        errors = {}
        return Response({"message": message, "data": pet_data, "status": status, "errors": errors})
