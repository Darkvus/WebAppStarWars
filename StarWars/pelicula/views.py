from django.views.generic import ListView, DetailView

from historial.models import Historial
from pelicula.models import Film
from personaje.models import Personaje


class ListViewPeli(ListView):
    model = Film
    template_name = "pelicula/lista.html"
    context_object_name = "peliculas"


    def dispatch(self, request, *args, **kwargs):
        Historial(url=request.path).save()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        if self.request.GET:
            context["Search"] = True
        else:
            context["Search"] = False

        return context

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.GET:
            return qs.filter(title__contains=self.request.GET['search']).order_by('episode_id')
        else:
            return qs.order_by('episode_id')

class DetailViewPeli(DetailView):
    template_name = "pelicula/detalle.html"
    model = Film

    def dispatch(self, request, *args, **kwargs):
        Historial(url=request.path).save()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personajes'] = Personaje.objects.filter(films=self.kwargs['pk'])
        return context
        