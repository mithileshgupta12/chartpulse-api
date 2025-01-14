from django.urls import path, include
from .views.auth.register_view import RegisterView
from .views.auth.login_view import LoginView
from .views.auth.me_view import MeView
from .views.auth.logout_view import LogoutView
from .views.auth.csrf_token_view import CsrfTokenView

urlpatterns = [
    path('auth/csrf-token/', CsrfTokenView.as_view(), name='csrf-token'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/me/', MeView.as_view(), name='me'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]