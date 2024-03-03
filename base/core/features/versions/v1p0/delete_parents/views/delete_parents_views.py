from rest_framework.response import Response
from rest_framework.views import APIView
from base.utilities.constant import *
from core.models import Parent
from django.http import Http404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
class DeleteParentsViews(APIView):
    cation_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    
    def get_parents(self, pk):
        try: 
            return Parent.objects.get (pk=pk)
        except Parent.DoesNotExist:
            raise Http404
    @extend_schema(
                   description = 'To delete parents',
                   summary = 'Delete Parents.'    
    )
    def delete(self, request,pk):
        
        
        errors = {}
        data = {}
        status = None
        parents = self.get_parents(pk)
        parents.delete()
        message = 'Successfully Deleted'
        status = no_content        
        return Response ({"Message": message, "data": data, "status": status, "errors": errors }, status)