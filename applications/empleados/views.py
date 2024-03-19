from django.shortcuts import render

from django.views.generic import ListView

#model
from .models import Empleado

# Create your views here.
"""
3.- Listar empleados por trabajo (TAREA)

5.- Listar habilidades de un empleado"""

#1.- Lista todos los empleados de la empresa
class ListAllEmpleados(ListView):
  template_name = 'persona/list_all.html'
  model = Empleado


#2.- Listar todos los empleados que pertenecen a un area de la empresa 
class ListByAreaEmpleado(ListView):
  template_name = 'persona/list_by_area.html'

  def get_queryset(self):
    area = self.kwargs['shorname']
    lista = Empleado.objects.filter(
      departamento__short_name=area
    )
    print(lista)
    return lista


#4.- Listar los empleados por palabra clave
class ListEmpleadosByKword(ListView):
  template_name = 'persona/by_kword.html'
  context_object_name = 'empleados'

  def get_queryset(self):
    print('*********')
    palabra_clave = self.request.GET.get("kword", '')
    print('====', palabra_clave)
    lista = Empleado.objects.filter(
      first_name = palabra_clave
    )
    print(lista)
    return lista 