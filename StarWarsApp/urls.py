from django.urls import path

from StarWarsApp.views.portal import IndexView
from StarWarsApp.views.pelicula import ListViewPeli, DetailViewPeli
from StarWarsApp.views.personaje import PersoanajeListView


urlpatterns = [
    path('portal/', IndexView.as_view(), name="portal"),
    path('portal/film/list', ListViewPeli.as_view(), name='film'),
    path('portal/film/detail/<int:pk>',
         DetailViewPeli.as_view(), name='film_detail'),
    path('portal/personajes/list', PersoanajeListView.as_view(), name='personaje'),

]
