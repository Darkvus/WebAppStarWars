from django.urls import path

from StarWarsApp.views.portal import IndexView, SearchView
from StarWarsApp.views.pelicula import ListViewPeli, DetailViewPeli
from StarWarsApp.views.personaje import PersonajeListView, PersonajeDetailView
from StarWarsApp.helper.utils import ajaxSearch

urlpatterns = [
    path('portal/', IndexView.as_view(), name="portal"),
    path('portal/film/list/', ListViewPeli.as_view(), name='film'),
    path('portal/film/detail/<int:pk>/',
         DetailViewPeli.as_view(), name='film_detail'),
    path('portal/personajes/list/', PersonajeListView.as_view(), name='personaje'),
    path('portal/personajes/detail/<int:pk>/',
         PersonajeDetailView.as_view(), name='character_detail'),
    path('search/', ajaxSearch),
    path('portal/search', SearchView.as_view(), name='search'),
]
