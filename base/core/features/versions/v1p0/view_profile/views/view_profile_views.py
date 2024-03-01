from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from base.utilities.constant import ok
from ..serializers.view_profile_serializer import ViewProfileSerializer
from drf_spectacular.utils import extend_schema
class ViewProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    @extend_schema(request = ViewProfileSerializer,
                   responses={ok: ViewProfileSerializer},
                   description = 'To Display pets with owner',
                   summary = 'Display all Pets.'
            
    )
    def get(self, request):
        user = request.user
        is_admin = user.is_staff
        serializer = ViewProfileSerializer(user)
        serialized_data = serializer.data
        message = 'Successful'
        serialized_data = serializer.data
        status_code = ok
        errors = {}
        role = "owner" if is_admin else "staff"
        return Response({
            "message": message,
            "data": serialized_data,
            "status": status_code,
            "errors": errors,
            "role": role  
        })