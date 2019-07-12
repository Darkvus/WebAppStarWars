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
from StarWarsApp.helper.utils import sortedReverseDictionary, breadcrumSession


class IndexView(TemplateView):
    template_name = "portal/index.html"

    def dispatch(self, request, *args, **kwargs):
        # Guardamos la página visitada en el historial
        try:
            breadcrumSession(request, 'Home')
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            print(e)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = sortedReverseDictionary(self.request.session['breadcrum'])
        context["breadcrumb_list"] = items
        return context


class PortalRedirectView(RedirectView):

    url = reverse_lazy('app:portal')


class SearchView(ListView):
    template_name = 'portal/search.html'
    model = Personaje

    def dispatch(self, request, *args, **kwargs):
        # Guardamos la página visitada en el historial

        breadcrumSession(request,  "Search to " +
                                   request.environ["QUERY_STRING"].split("=")[-1])

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["peliculas"] = Pelicula.objects.filter(
            title__contains=self.request.GET['search']).order_by('title')

        context["filtro_personaje"] = Personaje.objects.filter(
            nombre__contains=self.request.GET['search']).order_by('nombre')
        items = sortedReverseDictionary(self.request.session['breadcrum'])
        context["breadcrumb_list"] = items

        return context
