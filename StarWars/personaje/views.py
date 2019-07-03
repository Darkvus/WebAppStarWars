from django.views.generic import DetailView
from django.shortcuts import render

from personaje.models import Personaje
from historial.models import Historial

class PersoDetailView (DetailView):
    template_name = "personaje/detalle.html"
    model = Personaje

    def dispatch(self, request, *args, **kwargs):
        Historial(url=request.path).save()
        return super().dispatch(request, *args, **kwargs)
    
  
    