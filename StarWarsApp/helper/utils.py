from StarWarsApp.models.pelicula import Pelicula
from StarWarsApp.models.personaje import Personaje
import json
from django.http import HttpResponse


def ajaxSearch(request):
    q = request.GET.get('term', '')
    results = [{"text": r.title, "type": "film", "pk": r.id} for r in Pelicula.objects.filter(title__contains=q)] +\
        [{"text": r.nombre, "type": "personaje", "pk": r.id}
            for r in Personaje.objects.filter(nombre__contains=q)]
    data = json.dumps(results)

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
