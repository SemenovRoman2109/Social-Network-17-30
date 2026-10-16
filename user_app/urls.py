from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegistrationView.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('main/', MainView.as_view(), name = 'main'),
    path('confirm_code/', ConfirmCodeView.as_view(), name = 'confirm_code')
]
