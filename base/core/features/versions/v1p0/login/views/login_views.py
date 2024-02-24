from rest_framework.response import Response
from rest_framework.views import APIView
from base.utilities.constant import *
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from core.models import CustomUser 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiResponse
class LoginView(APIView):
    
    permission_classes = [AllowAny]
    @extend_schema(request = TokenObtainPairSerializer, description= 'To Login or Obtain Authorization Key', 
    responses= {ok: OpenApiResponse(response=TokenObtainPairSerializer, description= 'Login Succesfully'),
    bad_request: OpenApiResponse(description = 'Incorrect password, Password is required. No user found with the given email/username.',)})
    
   
    def post(self, request, format=None):
        errors = {}
        data = {}
        status = None
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if not username:
            errors['username'] = 'Please enter a username.'
            status = unauthorized
            return Response({"message": "Username required.", "status": status, "errors": errors })

        user = CustomUser.objects.filter(Q(username=username)).first()

        if user is None:
            raise AuthenticationFailed('No user found with the given email/username.')

        if not password:   
            raise AuthenticationFailed('Password is required.')

        if not user.check_password(password):   
            raise AuthenticationFailed('Incorrect password.')

        serializer = TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            refresh_token = RefreshToken.for_user(serializer.user)
            data = {
                'access_token': str(serializer.validated_data['access']),
                'refresh_token': str(refresh_token),
            }
            message =  'Successfully Login'
            status = ok
            return Response({"message": message, "data": data, "status": status, "errors": errors })
        
        status = unauthorized
        return Response(serializer.errors, status=status)