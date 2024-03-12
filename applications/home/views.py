from django.shortcuts import render
from django.views.generic import TemplateView, ListView

#modelo Prueba
from .models import Prueba

# Create your views here.
class IndexView(TemplateView):
  template_name = 'home/home.html'


class ListViewPrueba(ListView):
  template_name = 'home/list.html'
  queryset = ['a', 'b', 'c']
  context_object_name = 'lista_prueba'


class ModeloPruebaListView(ListView):
  model = Prueba
  template_name = "home/pruebas.html"
  context_object_name = 'lista_prueba'

