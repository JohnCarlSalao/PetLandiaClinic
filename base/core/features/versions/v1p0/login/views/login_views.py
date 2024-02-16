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
class LoginView(APIView):
    
    permission_classes = [AllowAny]
        
    def post(self, request, format=None):
        errors = {}
        data = {}
        status = None
        username= request.data['username']
        password = request.data['password']


        user = CustomUser.objects.filter(Q(username=username)).first()

        if user is None:
            raise AuthenticationFailed('No user found with the given email/username.')

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
            return Response ({"message": message, "data": data, "status": status, "errors": errors })
        status = unauthorized
        return Response(serializer.errors, status=status)