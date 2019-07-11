from StarWarsApp.models.pelicula import Pelicula
from StarWarsApp.models.personaje import Personaje
from StarWarsApp.models.historial import Historial
import json
from django.http import HttpResponse


def getBreadcrum():
    return Historial.objects.all().order_by('-id')[:10]


def deleteRepeatElements(x):
    return list(dict.fromkeys(x))


def checkRegistry(category):
    flag = False
    registros = Historial.objects.all().order_by('-id')[:10]

    for reg in registros:
        if reg.category == category:
            flag = True
            break
    return flag


def ajaxSearch(request):
    q = request.GET.get('term', '')
    results = [{"text": r.title, "type": "film", "pk": r.id} for r in Pelicula.objects.filter(title__contains=q)] +\
        [{"text": r.nombre, "type": "personaje", "pk": r.id}
            for r in Personaje.objects.filter(nombre__contains=q)]
    data = json.dumps(results)

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
