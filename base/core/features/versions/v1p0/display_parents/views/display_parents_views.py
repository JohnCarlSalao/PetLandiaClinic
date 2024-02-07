from rest_framework.views import APIView
from core.models import Parent
from base.utilities.constant import *
from rest_framework.response import Response
from ..serializers.display_serializers import DisplayParentSerializer
from django.http import Http404
import pytz


class DisplayParentViews(APIView):
    def get(self, request):
        parent = Parent.objects.all().values('id', 'first_name', 'last_name', 'occupation', 'contact_number', 'pets')
        data = {'parent':list(parent)}
        message = 'Success'
        status = ok
        return Response({"Message": message, "data": data, "status": status})

class DisplayParentDetailViews(APIView):
    def get_parent(self, pk):
        try: 
            return Parent.objects.get(pk=pk)
        except Parent.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        
        parent = self.get_parent(pk)
        serializer = DisplayParentSerializer(parent)
        data =serializer.data
        status = ok
        message = 'Results'
        errors = {}
        return Response({"message": message, "data": data, "status": status, "errors": errors})
