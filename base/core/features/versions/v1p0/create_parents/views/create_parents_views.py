from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Parent
from base.utilities.constant import *
from base.utilities.generate_uid import generate_uuid
from ..serializers.create_parents_serializers import CreateParentSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiExample
class CreateParentViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
   
    @extend_schema(
    request=CreateParentSerializers,
    description='To Create Parents.',
    summary='Create Parents.',
    examples=[OpenApiExample(
            name='Create Pet Example',
            value={
                'first_name': 'Ranxer ',
                'last_name': 'Balondo',
                'contact_number': '09292811165',
                'occupation': 'Ceo',
                 }
,
        )],
    )
    def post(self, request):
        serializer = CreateParentSerializers(data=request.data)
        data = {}
        errors = {}
        status = None
        message = None

        if serializer.is_valid():
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            occupation = request.data['occupation']
            contact_number = request.data['contact_number']
            
            # Check if a parent with the same contact number already exists
            existing_number = Parent.objects.filter(contact_number=contact_number).exists()
            if existing_number:
                existing_parent_record = Parent.objects.get(contact_number=contact_number)
                data = {
                    'id': existing_parent_record.id,
                    'first_name': existing_parent_record.first_name,
                    'last_name': existing_parent_record.last_name,
                    'occupation': existing_parent_record.occupation,
                    'contact_number': existing_parent_record.contact_number
                }
                status = bad_request
                message = "Record with the provided contact number already exists."
                return Response({"message": message, "data": data, "status": status},status)
            
            
            existing_parent = Parent.objects.filter(
                first_name=first_name,
                last_name=last_name,
                occupation=occupation
            ).exists()

            if existing_parent:
                existing_parent_record = Parent.objects.get(
                    first_name=first_name,
                    last_name=last_name,
                    occupation=occupation
                )
                data = {
                    'id': existing_parent_record.id,
                    'first_name': existing_parent_record.first_name,
                    'last_name': existing_parent_record.last_name,
                    'occupation': existing_parent_record.occupation,
                    'contact_number': existing_parent_record.contact_number
                }
                status = bad_request
                message = "Record with the provided details already exists."
                return Response({"message": message, "data": data, "status": status},status)

            uid = generate_uuid()
            parent = Parent.objects.create(
                id=uid,
                first_name=first_name,
                last_name=last_name,
                occupation=occupation,
                contact_number=contact_number
            )
            parent_data = {
                'id': parent.id,
                'first_name': parent.first_name,
                'last_name': parent.last_name,
                'occupation': parent.occupation,
                'contact_number': parent.contact_number
            }
            data = parent_data
            status = created
            message = "Successfully Created"
            return Response({"message": message, "data": data, "status": status, "errors": errors},status)
        
        errors = serializer.errors
        status = bad_request
        return Response({"message": message, "data": data, "status": status, "errors": errors},status)