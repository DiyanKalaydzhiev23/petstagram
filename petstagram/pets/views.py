from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetForm
from petstagram.pets.models import Pet, Like


class AllPetsView(views.ListView):
    model = Pet
    template_name = 'pet_list.html'
    context_object_name = 'pets'


class CreatePetView(views.CreateView):
    form_class = PetForm
    template_name = 'pet_create.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPetView(views.UpdateView):
    form_class = PetForm
    template_name = 'pet_edit.html'
    success_url = reverse_lazy('home')


class DeletePetView(views.DeleteView):
    form_class = PetForm
    template_name = 'pet_delete.html'
    success_url = reverse_lazy('home')


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    context = {
        'pet': pet,
        'comment_form': CommentForm(),
        'comments': pet.comment_set.all(),
    }

    return render(request, 'pet_detail.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet,
    )
    like.save()
    return redirect('list pets')


def comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = Comment(
            comment=form.cleaned_data['comment'],
            pet=pet,
        )
        comment.save()

    return redirect('pet details', pet.id)
