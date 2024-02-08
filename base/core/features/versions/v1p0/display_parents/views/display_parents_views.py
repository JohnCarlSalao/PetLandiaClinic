from rest_framework.views import APIView
from core.models import Parent
from base.utilities.constant import *
from rest_framework.response import Response
from ..serializers.display_serializers import ParentSerializer, DisplayParentSerializer
from django.http import Http404
import pytz


class DisplayParentViews(APIView):
    def get(self, request):
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        number_of_parents = parents.count()
        data = {"number_of_parents": number_of_parents,"parents": serializer.data}  # Create a nested dictionary
        message = 'Successfully retrieved'
        errors = {}
        status = ok 
        return Response({"message": message, "data": data, "status": status, "errors": errors})
class DisplayParentDetailViews(APIView):
    def get_parent(self, pk):
        try: 
            return Parent.objects.get(pk=pk)
        except Parent.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        
        parent = self.get_parent(pk)
        serializer = ParentSerializer(parent)
        data =serializer.data
        status = ok
        message = 'Results'
        errors = {}
        return Response({"message": message, "data": data, "status": status, "errors": errors})
