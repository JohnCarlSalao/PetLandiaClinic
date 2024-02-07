from rest_framework.views import APIView
from core.models import Pets
from base.utilities.constant import *
from rest_framework.response import Response
from ..serializers.display_serializers import DisplayPetSerializer
from django.http import Http404
import pytz


class DisplayPetViews(APIView):
    def get(self, request):
        pets = Pets.objects.all().values('id','name','species', 'breed', 'color_or_markings', 'birthday','sex')
        data = {'pet':list(pets)}
         
        message = 'Success'
        status = ok
        return Response({"Message": message, "data": data, "status": status})

class DisplayPetDetailViews(APIView):
    def get_pet(self, pk):
        try: 
            return Pets.objects.get(pk=pk)
        except Pets.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        
        pets = self.get_pet(pk)
        serializer = DisplayPetSerializer(pets)
        data = {'pet': serializer.data}
        status = ok
        message = 'Results'
        errors = {}
        return Response({"message": message, "data": data, "status": status, "errors": errors})
