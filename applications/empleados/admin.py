from django.contrib import admin

from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)
admin.site.register(Empleado)
