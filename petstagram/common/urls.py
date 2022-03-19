from django.urls import path
from petstagram.common.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
