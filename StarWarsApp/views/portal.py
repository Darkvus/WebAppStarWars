import requests

from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, ListView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
import logging

from StarWarsApp.models.historial import Historial
from StarWarsApp.models.personaje import Personaje
from StarWarsApp.models.pelicula import Pelicula


class IndexView(TemplateView):

    def get(self, request):
        self.template_name = "portal/index.html"
        return render(request, self.template_name, {})

    def dispatch(self, request, *args, **kwargs):
        # Guardamos la página visitada en el historial
        Historial(url=request.path).save()
        return super().dispatch(request, *args, **kwargs)


class PortalRedirectView(RedirectView):

    url = reverse_lazy('app:portal')


class SearchView(ListView):
    template_name = 'portal/search.html'
    model = Personaje

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["peliculas"] = Pelicula.objects.filter(
            title__contains=self.request.GET['search']).order_by('title')

        context["filtro_personaje"] = Personaje.objects.filter(
            nombre__contains=self.request.GET['search']).order_by('nombre')
        return context
