from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        try:
            logout(request)

            return Response({
                "message": "Logged out successfully."
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Could not log out user',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
