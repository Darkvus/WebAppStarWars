import requests

from django.views.generic import TemplateView, RedirectView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
import logging

from historial.models import Historial
from base.services import LoadData as ld


class IndexView(TemplateView):
    
    def get(self, requests):
        self.template_name = "base/index.html"
        render(request,"carts/home.html",{})
    
    def dispatch(self, request, *args, **kwargs):
        # Guardamos la página visitada en el historial
        Historial(url=request.path).save()
        return super().dispatch(request, *args, **kwargs)


class ApiToDB(RedirectView):

    def dispatch(self, request, *args, **kwargs):
        # Poblar la base de datos obtendios de la Api
        url_reverse = reverse_lazy('index')
        success_message = 'La ha cargado los datos'

        Historial(url=request.path).save()
        try:
            ld.execute()
            messages.success(request, 'La BD ha sido poblada')

        except Exception as e:
            logging.error('La carga de datos a fallado')
            messages.error(request, 'La carga de datos a fallado. ¡INTENTALO MÁS TARDE!')
            print(e)

        return HttpResponseRedirect(url_reverse)
