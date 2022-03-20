from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models
from petstagram.accounts.managers import PetstagramUserManager

'''
1. Create model extending...
2. Configure this model in settings.py
3. Create user manager
'''


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(
        max_length=25,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff =  models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()


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
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
