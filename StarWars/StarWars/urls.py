"""StarWars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from base import views as base
from pelicula import urls as pelicula_urls
from historial import views as historial_view
from personaje import views as personaje_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base.IndexView.as_view(), name="index"),
    path('apitodb/', base.ApiToDB.as_view(), name='ApitoDb'),
    path('peliculas/', include((pelicula_urls, 'pelicula'), namespace="pelicula")),
    path('historial/', historial_view.ListViewHistorial.as_view(), name="historial"),
    path('personaje/detail/<int:pk>/', personaje_view.PersoDetailView.as_view(), name="detailpers"),

]
