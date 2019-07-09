from django.views.generic import DetailView
from django.shortcuts import render

from StarWarsApp.models.personaje import Personaje
from StarWarsApp.models.historial import Historial


class PersoanajeListView (DetailView):
    template_name = "personaje/detalle.html"
    model = Personaje

    def dispatch(self, request, *args, **kwargs):
        Historial(url=request.path).save()
        return super().dispatch(request, *args, **kwargs)
