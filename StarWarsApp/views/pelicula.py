from django.views.generic import ListView, DetailView

from StarWarsApp.models.historial import Historial
from StarWarsApp.models.pelicula import Pelicula
from StarWarsApp.models.personaje import Personaje

from StarWarsApp.helper.utils import sortedReverseDictionary, breadcrumSession


class ListViewPeli(ListView):
    model = Pelicula
    template_name = "pelicula/lista.html"
    context_object_name = "peliculas"

    def dispatch(self, request, *args, **kwargs):
        breadcrumSession(request, 'List of Film')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        if self.request.GET:
            context["Search"] = True
        else:
            context["Search"] = False

        items = sortedReverseDictionary(self.request.session['breadcrum'])
        context["breadcrumb_list"] = items
        return context

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.GET:
            return qs.filter(title__contains=self.request.GET['search']).order_by('episode_id')
        else:
            return qs.order_by('episode_id')


class DetailViewPeli(DetailView):
    template_name = "pelicula/detalle.html"
    model = Pelicula

    def dispatch(self, request, *args, **kwargs):
        film = Pelicula.objects.get(id=self.kwargs['pk'])
        breadcrumSession(request, film.title)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personajes'] = Personaje.objects.filter(
            peliculas=self.kwargs['pk'])
        items = sortedReverseDictionary(self.request.session['breadcrum'])
        context["breadcrumb_list"] = items
        return context
