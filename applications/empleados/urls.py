from django.urls import path

#importacion de la vista
from . import views

#esto hace referencia a todas las urls que estan declaradas
app_name = "empleado_app"


urlpatterns = [
  path('listar-todo-empleados', views.ListAllEmpleados.as_view()),
  path('lista-by-area/<shorname>', views.ListByAreaEmpleado.as_view()),
  path('lista-by-job/<job>', views.ListByEmpleadoJob.as_view()),
  path('buscar-empleado', views.ListEmpleadosByKword.as_view()),
  path('lista-habilidades-empleados', views.ListHabilidadesEmpleado.as_view()),
  path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view()),
  path('add-empledo/', views.EmpleadoCreateView.as_view()),
  path('success/', views.SuccessView.as_view(), name='correcto'),
]