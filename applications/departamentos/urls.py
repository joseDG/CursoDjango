from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('new-departamento/',views.NewDepartamentoView.as_view(), name='new_departamento' ),
]
