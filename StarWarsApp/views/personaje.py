from django.views.generic import DetailView, ListView
from django.shortcuts import render

from StarWarsApp.models.personaje import Personaje
from StarWarsApp.models.historial import Historial


class PersonajeListView (ListView):
    template_name = "personaje/listar.html"
    model = Personaje
    context_object_name = "personajes"

    def dispatch(self, request, *args, **kwargs):
        Historial(url=request.path).save()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()

        return qs.order_by('nombre')


class PersonajeDetailView(DetailView):
    model = Personaje
    template_name = 'personaje/detalle.html'
