from django.views.generic import ListView, DetailView

from StarWarsApp.models.historial import Historial
from StarWarsApp.models.pelicula import Pelicula
from StarWarsApp.models.personaje import Personaje

from StarWarsApp.helper.utils import checkRegistry


class ListViewPeli(ListView):
    model = Pelicula
    template_name = "pelicula/lista.html"
    context_object_name = "peliculas"

    def dispatch(self, request, *args, **kwargs):
        registro = checkRegistry("Film List")

        if not registro:
            Historial(url=request.path, category="Film List").save()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        if self.request.GET:
            context["Search"] = True
        else:
            context["Search"] = False

        context["breadcrumb_list"] = Historial.objects.all().order_by(
            '-id')[:10]
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
        registro = checkRegistry(film.title)

        if not registro:

            Historial(url=request.path, category=film.title).save()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personajes'] = Personaje.objects.filter(
            peliculas=self.kwargs['pk'])
        context["breadcrumb_list"] = Historial.objects.all().order_by(
            '-id')[:10]
        return context
