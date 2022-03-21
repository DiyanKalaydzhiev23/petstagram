from django.urls import path

from petstagram.accounts.views import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),

    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),

    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile'),
    path('edit/', EditProfileView.as_view(), name='edit view'),
]
