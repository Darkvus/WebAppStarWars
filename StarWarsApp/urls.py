from django.urls import path

from StarWarsApp.views.portal import IndexView
from StarWarsApp.views.pelicula import ListViewPeli

urlpatterns = [
    path('portal/', IndexView.as_view(), name="portal"),
    path('portal/film/', ListViewPeli.as_view(), name='pelicula'),
]
