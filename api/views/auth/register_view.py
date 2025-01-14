from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from ...validators.auth.post_register_validator import PostRegisterValidator
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request: Request):
        return

class RegisterView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request: Request) -> Response:
        validator = PostRegisterValidator(data=request.data)

        if not validator.is_valid():
            return Response(
                data=validator.errors,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        
        validated_data = validator.validated_data

        try:
            user = User.objects.create_user(
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    username=validated_data['username'],
                    email=validated_data['email'],
                    password=validated_data['password']
                )
            
            return Response({
                'message': 'User registered successfully.'
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'message': 'Could not create user',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
