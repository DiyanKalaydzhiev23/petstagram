from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from petstagram.common.view_mixins import RedirectToAllPets


class UserRegisterView(RedirectToAllPets):
    pass


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('list pets')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserDetailsView:
    pass


class EditProfileView:
    pass


class ChangeUserPasswordView:
    pass
