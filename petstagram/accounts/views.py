from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from petstagram.accounts.forms import CreateProfileForm
from petstagram.common.view_mixins import RedirectToAllPets
from petstagram.accounts.models import Profile
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from petstagram.pets.models import Pet


class UserRegisterView(RedirectToAllPets, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('list pets')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('list pets')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView(views.UpdateView):
    pass


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    success_url = reverse_lazy('list pets')
    template_name = 'accounts/change_password.html'


class ProfileDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
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
