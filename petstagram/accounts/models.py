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
