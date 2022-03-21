from django.urls import path
from petstagram.pets.views import *

urlpatterns = [
    path('', AllPetsView.as_view(), name='list pets'),

    path('create/', CreatePetView.as_view(), name='create pet'),
    path('edit/<int:pk>', EditPetView.as_view(), name='edit pet'),
    path('delete/<int:pk>', DeletePetView.as_view(), name='delete pet'),
    path('details/<int:pk>', PetDetailsView.as_view(), name='pet details'),
    path('like/<int:pk>', like_pet, name='like pet'),
    path('comment/<int:pk>', comment_pet, name='comment pet'),
]
