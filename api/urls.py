from django.urls import path, include
from .views.auth.register_view import RegisterView
from .views.auth.login_view import LoginView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
]