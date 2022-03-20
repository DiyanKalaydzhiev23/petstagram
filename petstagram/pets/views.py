from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import redirect

from petstagram.accounts.models import Profile
from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetForm
from petstagram.pets.models import Pet, Like


class AllPetsView(views.ListView):
    model = Pet
    template_name = 'pet_list.html'
    context_object_name = 'pets'


class CreatePetView(views.CreateView, auth_mixins.LoginRequiredMixin):
    form_class = PetForm
    template_name = 'pet_create.html'
    success_url = reverse_lazy('list pets')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPetView(views.UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet_edit.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class DeletePetView(views.DeleteView):
    form_class = PetForm
    template_name = 'pet_delete.html'
    success_url = reverse_lazy('home')


class PetDetailsView(views.DetailView, auth_mixins.LoginRequiredMixin):
    model = Pet
    template_name = 'pet_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet'] = self.object
        context['is_owner'] = self.object.user_profile == self.request.user
        context['likes_count'] = self.object.like_set.count()
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comment_set.all()
        return context


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


class ProfileDetailsView(views.DetailView, auth_mixins.LoginRequiredMixin):
    model = Profile
    template_name = 'accounts/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = list(Pet.objects.filter(user_profile=self.object.user))
        total_likes_count = sum(p.like_set.count() for p in pets)
        total_pets = len(pets)

        context.update({
            'profile': self.object,
            'is_owner': self.object.user.id == self.request.user.id,
            'total_likes_count': total_likes_count,
            'total_pets': total_pets,
            'pets': pets,
        })

        return context
