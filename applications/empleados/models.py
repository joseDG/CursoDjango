from django.db import models

#modelo Departamento
from applications.departamentos.models import Departamento

# Create your models here.
class Habilidades(models.Model):
  habilidad = models.CharField('Habilidades', max_length=50)

  def __str__(self):
    return str(self.id) + ' - ' + self.habilidad


class Empleado(models.Model):
  """ Modelo para la tabla empleado"""

  #Contador
  #Administrador
  #Economistaa
  #Otro
  JOB_CHOICES = (
    ('0', 'Contador'),
    ('1', 'Administrador'),
    ('2', 'Economista'),
    ('3', 'Otro'),
  )

  first_name = models.CharField('Nombres', max_length=60)
  last_name = models.CharField('Apellidos', max_length=60)
  job = models.CharField('Puesto de Trabajo', max_length=1, choices=JOB_CHOICES)
  #imagen = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
  departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
  habilidades = models.ManyToManyField(Habilidades)

  def __str__(self):
    return self.first_name 

  
