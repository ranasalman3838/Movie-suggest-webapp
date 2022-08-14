from django.urls import path
from .import views

urlpatterns = [
    path('', views.start, name="start"),
    path('index/', views.index, name="index"),
    path('final/', views.final, name="final"),
    path('movies/', views.movies, name="movies")

]