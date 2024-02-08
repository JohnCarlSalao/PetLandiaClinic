from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Parent
from base.utilities.constant import *
from base.utilities.generate_uid import generate_uuid
from ..serializers.create_parents_serializers import CreateParentSerializers
class CreateParentViews(APIView):
    def post (self, request):

        serializers =  CreateParentSerializers (data=request.data)
        data={}
        errors ={}
        status = None
        message = None

        if serializers.is_valid():
            uid = generate_uuid()
            parent = Parent.objects.create(id=uid,
                                           first_name =request.data ['first_name'],
                                           last_name =request.data ['last_name'],
                                           occupation =request.data ['occupation'],
                                           contact_number= request.data['contact_number'])
            parent_data= parent
            parent_data = Parent.objects.filter(id=uid).values('id', 'first_name', 'last_name', 'occupation','contact_number')
            data = parent_data
            errors =serializers.errors
            status = created
            message = 'Successfully Created'
            return Response({"message": message, "data": data, "status": status, "errors": errors})
        
        errors = serializers.errors
        status =bad_request
        return Response({"message": message, "data": data, "status": status, "errors": errors})