from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

class MeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request) -> Response:
        user = request.user

        try:
            return Response(data={
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'email': user.email,
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Could not fetch user data',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
