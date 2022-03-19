from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models


UserModel = get_user_model()


class Profile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
        )
    )

    last_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
        )
    )

    picture = models.URLField()

    date_of_birth = models.DateTimeField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SHOW,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DOG, 'Dog'),
        (TYPE_CHOICE_CAT, 'Cat'),
        (TYPE_CHOICE_PARROT, 'Parrot')
    )

    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES
    )
    name = models.CharField(
        max_length=6
    )
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(
        upload_to='images',
    )

    user_profile = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
