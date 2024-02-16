from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Pets
from base.utilities.constant import  *
from base.utilities.generate_uid import generate_uuid
from ..serializers.create_pets_serializers import CreatePetsSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
class CreatePetsViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes  = [IsAuthenticated]
    def post (self, request):
        serializers  = CreatePetsSerializers (data= request.data)
       
        if serializers.is_valid():
            
            uid = generate_uuid()
            pet_data= Pets.objects.create(id = uid, 
                                    name = request.data ['name'],
                                    species = request.data ['species'],
                                    breed = request.data ['breed'],
                                    color_or_markings =request.data ['color_or_markings'],
                                    birthday=serializers.validated_data['birthday'],
                                    sex = request.data['sex'])                                  
            pet_data = Pets.objects.filter(id=uid).values('id','name','species', 'breed', 'color_or_markings', 'birthday','sex')
            data = pet_data
            errors = serializers.errors
            status = created 
            message = 'Succesfully Created'
            return Response({"message":message,"data": data,  "status": status, "errors": errors})
        else:
            errors = serializers.errors
            status = bad_request
            return Response({"status": status, "errors": errors})


