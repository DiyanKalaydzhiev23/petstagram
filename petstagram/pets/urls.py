from django.urls import path
from petstagram.pets.views import *

urlpatterns = [
    path('', list_pets, name='list pets'),
    path('create/', create_pet, name='create pet'),
    path('edit/<int:pk>', edit_pet, name='edit pet'),
    path('delete/<int:pk>', delete_pet, name='delete pet'),
    path('details/<int:pk>', pet_details, name='pet details'),
    path('like/<int:pk>', like_pet, name='like pet'),
    path('comment/<int:pk>', comment_pet, name='comment pet')
]
