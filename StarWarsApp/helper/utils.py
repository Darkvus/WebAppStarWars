from StarWarsApp.models.pelicula import Pelicula
from StarWarsApp.models.personaje import Personaje
from StarWarsApp.models.historial import Historial
import json
from django.http import HttpResponse
import string
import random


def getBreadcrum():
    return Historial.objects.all().order_by('-id')[:10]


def generateCookie():
    return ''.join(random.choice(string.ascii_letters+string.digits) for i in range(50))


def checkRegistry(category, cookie):
    flag = False
    registros = Historial.objects.all().order_by('-id')[:10]

    for reg in registros:
        if reg.category == category and reg.cookie == cookie:
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


def breadcrumSession(request, friendly_form):
    # try:
    #     dic = request.session['breadcrum']
    #     del request.session['breadcrum']
    #     dic.pop(request.path, None)
    #     dic[request.path] = friendly_form
    #     request.session['breadcrum'] = dic
    # except:
    #     request.session['breadcrum'] = {request.path: friendly_form}

    try:
        dic = request.session['breadcrum']
        dic.pop(request.path, None)
        dic[request.path] = friendly_form
        request.session['breadcrum'] = dic
        request.session.modified = True

    except:
        request.session['breadcrum'] = {request.path: friendly_form}


def sortedReverseDictionary(dict):
    list_last = list(dict)[-10:][::-1]
    aux = {}
    for i in list_last:
        aux[i] = dict[i]
    return aux
