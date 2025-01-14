from django.urls import path, include
from .views.auth.register_view import RegisterView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
]