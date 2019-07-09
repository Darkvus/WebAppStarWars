from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.urls import reverse_lazy
import logging
import json
from django.contrib import messages

from braces.views import LoginRequiredMixin
from StarWarsApp.services.load_data import LoadData as ld
from StarWarsApp.helper.exception import LoadDataException
from StarWarsApp.models.historial import Historial
from StarWarsApp.models.pelicula import Pelicula
from StarWarsApp.models.personaje import Personaje


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "manager/index.html"
    login_url = "accounts/login"
    raise_exception = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["personajes"] = Personaje.objects.all().count()
        context["peliculas"] = Pelicula.objects.all().count()
        return context


class DataLoad(View):

    def dispatch(self, request, *args, **kwargs):
        # Poblar la portal de datos obtendios de la Api
        url_reverse = reverse_lazy('homeAdmin')
        success_message = 'La ha cargado los datos'

        Historial(url=request.path).save()
        try:
            ld.execute()
            context = {'personajes': Personaje.objects.all(
            ).count(), 'peliculas': Pelicula.objects.all().count()}
            messages.success(
                request, "La operación ha sido realizada con exito")
            return HttpResponse(content=json.dumps({'message': 'La operación ha sido realizada con exito', 'context': context}), content_type='application/json')

        except LoadDataException as ls_excep:
            return HttpResponseBadRequest(content=json.dumps({'message': str(ls_excep)}), content_type='application/json')

        except Exception as e:
            messages.error(
                request, "La operación no se ha podido completar pongase en contacto con el administrador")
            return HttpResponseBadRequest(content=json.dumps({'message': 'La operación no se ha podido completar pongase en contacto con el administrador'}), content_type='application/json')
            logging.exception(e)

        return HttpResponseRedirect(url_reverse)
