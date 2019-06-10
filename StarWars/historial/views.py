from django.views.generic import ListView

from historial.models import Historial


class ListViewHistorial(ListView):
    model = Historial
    template_name = "historial/list.html"
    context_object_name = "historiales"

    def dispatch(self, request, *args, **kwargs):
        Historial(url=request.path).save()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().order_by('date')
