from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Parent, Pets
from ..serializers.edit_parent_serializers import EditParentSerializer
from base.utilities.constant import *
from django.http import Http404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
class EditParentViews(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    

    def get_parent(self, pk):
        try:
            return Parent.objects.get(pk=pk)
        except Parent.DoesNotExist:
            raise Http404
    @extend_schema(request = EditParentSerializer,
                   
                   responses={ok: EditParentSerializer},
                   description = 'To Edit Parents.',
                   summary = 'Editing Parents via id.',
                   examples=[OpenApiExample(
            name='Edit Parentt Example',
            value={
                'first_name': 'Joshua',
                'last_name': 'Penny',
                'contact_number': '096788888',
                'occupation':'M',
      })]
            
    )
    def put(self, request, pk):
        data = {}
        errors = {}
        status = None
        message = None
        parent = self.get_parent(pk)
        data = request.data.copy()

        
        data.setdefault('first_name', parent.first_name)
        data.setdefault('last_name', parent.last_name)
        data.setdefault('contact_number', parent.contact_number)
        data.setdefault('occupation', parent.occupation)

        
        pets_data = data.get('pets', [])
        if not isinstance(pets_data, list):
            pets_data = [pets_data] 
        
        
        data['pets'] = pets_data

        serializer = EditParentSerializer(parent, data=data, partial=True)
        

        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            data = {'parent': serializer.data}
            status = ok
            return Response({"message": 'Successfully Updated', "data": data, "status": status},status)
        else:
            status = bad_request
            data = serializer.data
            errors = serializer.errors
            return Response({"message": 'Error', "data": data, "status": status, "errors": errors},status)

