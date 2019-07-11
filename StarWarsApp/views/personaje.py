from django.views.generic import DetailView, ListView
from django.shortcuts import render

from StarWarsApp.models.personaje import Personaje
from StarWarsApp.models.historial import Historial
from StarWarsApp.helper.utils import checkRegistry


class PersonajeListView (ListView):
    template_name = "personaje/listar.html"
    model = Personaje
    context_object_name = "personajes"

    def dispatch(self, request, *args, **kwargs):
        registro = checkRegistry("Characters List")
        if not registro:
            Historial(url=request.path, category="Characters List").save()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()

        return qs.order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumb_list"] = Historial.objects.all().order_by('-id')[:10]
        return context


class PersonajeDetailView(DetailView):
    model = Personaje
    template_name = 'personaje/detalle.html'

    def dispatch(self, request, *args, **kwargs):
        # Guardamos la página visitada en el historial
        personaje = Personaje.objects.get(id=self.kwargs['pk'])
        registro = checkRegistry(personaje.nombre)
        if not registro:
            Historial(url=request.path, category=personaje.nombre).save()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumb_list"] = Historial.objects.all().order_by('-id')[:10]
        return context
