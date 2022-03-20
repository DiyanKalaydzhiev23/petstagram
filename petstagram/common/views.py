from django.shortcuts import redirect
from django.views import generic as views

from petstagram.common import view_mixins


class HomeView(view_mixins.RedirectToAllPets, views.TemplateView):
    template_name = 'landing_page.html'
