from django.urls import path

#importacion de la vista
from . import views


urlpatterns = [
  path('home/', views.IndexView.as_view()),
  path('lista/', views.ListViewPrueba.as_view()),
  path('lista-prueba', views.ModeloPruebaListView.as_view()),
  path('add/', views.PruebaCreateView.as_view())
]
