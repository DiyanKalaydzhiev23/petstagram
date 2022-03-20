from django.shortcuts import redirect


class RedirectToAllPets:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('list pets')

        return super().dispatch(request, *args, **kwargs)