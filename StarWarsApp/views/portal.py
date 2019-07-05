import requests

from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
import logging

from StarWarsApp.models.historial import Historial
from StarWarsApp.services.loaddata import LoadData as ld


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


class ApiToDB(RedirectView):

    def dispatch(self, request, *args, **kwargs):
        # Poblar la portal de datos obtendios de la Api
        url_reverse = reverse_lazy('index')
        success_message = 'La ha cargado los datos'

        Historial(url=request.path).save()
        try:
            ld.execute()
            messages.success(request, 'La BD ha sido poblada')

        except Exception as e:
            logging.error(
                '------------------------------ La carga de datos a fallado -------------------------------')
            messages.error(
                request, 'WOOOOOOOOOOOOOOOOOOOOOOOO La carga de datos a fallado. ¡INTENTALO MÁS TARDE! ;(')
            print(e)

        return HttpResponseRedirect(url_reverse)
