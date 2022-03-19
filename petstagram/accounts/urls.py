from django.urls import path

from petstagram.accounts.views import UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login user'),
]
