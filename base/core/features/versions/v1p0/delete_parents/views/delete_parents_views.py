from rest_framework.response import Response
from rest_framework.views import APIView
from base.utilities.constant import *
from core.models import Parent
from django.http import Http404


class DeleteParentsViews(APIView):

    
    def get_parents(self, pk):
        try: 
            return Parent.objects.get (pk=pk)
        except Parent.DoesNotExist:
            raise Http404
    def delete(self, request,pk):
        
        errors = {}
        data = {}
        status = None
        parents = self.get_parents(pk)
        parents.delete()
        message = 'Successfully Deleted'
        status = no_content        
        return Response ({"Message": message, "data": data, "status": status, "errors": errors })