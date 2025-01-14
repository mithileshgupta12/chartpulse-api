from django.urls import path, include
from .views.auth.register_view import RegisterView
from .views.auth.login_view import LoginView
from .views.auth.me_view import MeView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/me/', MeView.as_view(), name='me'),
]