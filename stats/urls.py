from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name="about"),
    path('import_csv', views.import_csv, name='import_csv'),
    path('letterboxd', views.letterboxd, name='letterboxd'),
    path('imdb', views.imdb, name="imdb"),
]