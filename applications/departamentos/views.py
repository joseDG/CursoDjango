from django.shortcuts import render
from django.views.generic.edit import FormView

#form
from .forms import NewDepartamentoForm

#importacion de modelos
from applications.empleados.models import Empleado
from .models import Departamento

# Create your views here.
class NewDepartamentoView(FormView):
  template_name = 'departamento/new_departamento.html'
  form_class = NewDepartamentoForm
  success_url = '/'

  def form_valid(self, form):
    print('*******************ESTAMOS EN EL FORM VALID***************')

    depa = Departamento(
      name = form.cleaned_data['departamento'],
      short_name = form.cleaned_data['shorname'] 
    )
    depa.save()

    nombre = form.cleaned_data['nombre']
    apellido = form.cleaned_data['apellidos']

    Empleado.objects.create(
      first_name = nombre,
      last_name = apellido,
      job='3',
      departamento = depa
    )

    return super(NewDepartamentoView, self).form_valid(form)
