from django.shortcuts import render, redirect
from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetForm
from petstagram.pets.models import Pet, Like


def post_data(request, instance):
    form = PetForm(request.POST, request.FILES, instance=instance)

    if form.is_valid():
        form.save()
        return redirect('list pets')


def list_pets(request):
    context = {
        'pets': Pet.objects.all()
    }

    return render(request, 'pet_list.html', context)


def create_pet(request):
    if request.method == 'POST':
        return post_data(request, None)

    context = {
        'form': PetForm(),
    }

    return render(request, 'pet_create.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    context = {
        'pet': pet,
        'comment_form': CommentForm(),
        'comments': pet.comment_set.all(),
    }

    return render(request, 'pet_detail.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == 'POST':
        return post_data(request, pet)

    context = {
        'form': PetForm(instance=pet),
        'pk': pk
    }

    return render(request, 'pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == 'POST':
        pet.delete()
        return redirect('list pets')

    context = {
        'pk': pk,
    }

    return render(request, 'pet_delete.html', context)


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
