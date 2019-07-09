import requests

from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
import logging

from StarWarsApp.models.historial import Historial


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
