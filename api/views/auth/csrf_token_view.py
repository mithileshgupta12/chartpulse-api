from django.middleware.csrf import get_token
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

class CsrfTokenView(APIView):
    def get(self, request: Request) -> Response:
        return Response({
            'csrfToken': get_token(request)
        })