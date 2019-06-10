from django.urls import path

from pelicula.views import ListViewPeli, DetailViewPeli

urlpatterns = [
    path('list/', ListViewPeli.as_view(), name="list"),
    path('detail/<int:pk>/', DetailViewPeli.as_view(), name="detail")
]
