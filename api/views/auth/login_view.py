from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from ...validators.auth.post_login_validator import PostLoginValidator
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.authentication import SessionAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request: Request):
        return

class LoginView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request: Request) -> Response:
        validator = PostLoginValidator(data=request.data)

        if not validator.is_valid():
            return Response(
                data=validator.errors,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        
        validated_data = validator.validated_data

        try:
            authenticated_user = authenticate(
                username=validated_data['username'],
                password=validated_data['password']
            )

            if not authenticated_user:
                return Response(data={
                    "message": "Invalid credentials."
                }, status=status.HTTP_401_UNAUTHORIZED)
            
            login(request, authenticated_user)

            return Response(data={
                "message": "Logged in successfully."
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={
                'message': 'Could not login user',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
