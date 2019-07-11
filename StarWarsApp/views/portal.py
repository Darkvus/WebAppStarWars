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
from StarWarsApp.helper.utils import checkRegistry


class IndexView(TemplateView):
    template_name = "portal/index.html"

    def dispatch(self, request, *args, **kwargs):
        # Guardamos la página visitada en el historial
        registro = checkRegistry("Home")

        if not registro:
            Historial(url=request.path, category="Home").save()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumb_list"] = Historial.objects.all().order_by('-id')[:10]
        return context


class PortalRedirectView(RedirectView):

    url = reverse_lazy('app:portal')


class SearchView(ListView):
    template_name = 'portal/search.html'
    model = Personaje

    def dispatch(self, request, *args, **kwargs):
        # Guardamos la página visitada en el historial
        registro = checkRegistry(
            "Search to "+request.environ["QUERY_STRING"].split("=")[-1])

        if not registro:
            Historial(url=request.environ["PATH_INFO"]+"?" +
                      request.environ["QUERY_STRING"], category="Search to "+request.environ["QUERY_STRING"].split("=")[-1]).save()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["peliculas"] = Pelicula.objects.filter(
            title__contains=self.request.GET['search']).order_by('title')

        context["filtro_personaje"] = Personaje.objects.filter(
            nombre__contains=self.request.GET['search']).order_by('nombre')
        context["breadcrumb_list"] = Historial.objects.all().order_by('-id')[:10]
        return context
