from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
  ListView, 
  DetailView, 
  CreateView, 
  TemplateView, 
  UpdateView,
  DeleteView
  )

#model
from .models import Empleado

# Create your views here.
#1.- Lista todos los empleados de la empresa
class ListAllEmpleados(ListView):
  template_name = 'persona/list_all.html'
  paginate_by = 4
  ordering = 'first_name'
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

#3.- Listar empleados por trabajo (TAREA)
class ListByEmpleadoJob(ListView):
  template_name = 'persona/list_by_job.html'

  def get_queryset(self):
    trabajo = self.kwargs['job']
    if self.kwargs['job'] == 'Contador':
      trabajo = '0'
    elif self.kwargs['job'] == 'Administrador':
      trabajo = '1'
    elif self.kwargs['job'] == 'Economista':
      trabajo = '2'

    elif self.kwargs['job'] == 'Otro':
      trabajo = '3'

    lista = Empleado.objects.filter(
      job = trabajo
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

#5.- Listar habilidades de un empleado
#ListView con la relacion ManyToMany
class ListHabilidadesEmpleado(ListView):
  template_name = 'persona/habilidades.html'
  context_object_name = 'habilidades'

  def get_queryset(self):
    empleado = Empleado.objects.get(id=3)
    print()
    return empleado.habilidades.all()
  
#DetailView
class EmpleadoDetailView(DetailView):
  model = Empleado
  template_name = 'persona/detail_empleado.html'

  
  def get_context_data(self, **kwargs):
      context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
      context['titulo'] = 'Empleado del mes'
      return context
    
#uso del templateView
class SuccessView(TemplateView):
  template_name = 'persona/success.html'

# uso del createView 
class EmpleadoCreateView(CreateView):
  template_name = 'persona/add.html'
  model = Empleado
  fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
  success_url = reverse_lazy('empleado_app:correcto')

  def form_valid(self, form):
      empleado = form.save(commit=False)
      empleado.full_name = empleado.first_name + ' ' + empleado.last_name
      empleado.save()
      return super(EmpleadoCreateView, self).form_valid(form)
  
#crear el updateView
class EmpleadoUpdateView(UpdateView):
  template_name = "persona/update.html"
  model = Empleado
  fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
  success_url = reverse_lazy('empleado_app:correcto')

  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    print('****METODO POST*******')
    return super().post(request, *args, **kwargs)

  def form_valid(self, form):
      print('*******METODO FORM VALID***********')
      return super(EmpleadoUpdateView, self).form_valid(form)
  

#crear el DeleteView
class EmpleadoDeleteView(DeleteView):
  model = Empleado
  template_name = "persona/delete.html"
  success_url = reverse_lazy('empleado_app:correcto')