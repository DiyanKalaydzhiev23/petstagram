from django.shortcuts import redirect
from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'landing_page.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('list pets')

        return super().dispatch(request, *args, **kwargs)
