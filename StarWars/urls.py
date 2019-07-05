"""StarWars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-portald views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from StarWarsApp import urls as url_app
from StarWarsApp.views.portal import PortalRedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include((url_app, 'app'), namespace="app")),
    path('', PortalRedirectView.as_view(), name='index'),

    # path('apitodb/', portal.ApiToDB.as_view(), name='ApitoDb'),
    # path('peliculas/', include((pelicula_urls, 'pelicula'), namespace="pelicula")),
    # path('historial/', historial_view.ListViewHistorial.as_view(), name="historial"),
    # path('personaje/detail/<int:pk>/',
    #   personaje_view.PersoDetailView.as_view(), name="detailpers"),
]
