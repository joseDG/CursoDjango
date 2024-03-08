from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return render(request,'index.html' , {
    #contex
    'title': 'Curso Django',
    'message': 'Productos',
    'products': [
      {'title': 'Camisa', 'price': 50, 'stock': True},
      {'title': 'Pantalon', 'price': 100, 'stock': False},
      {'title': 'Gafas', 'price': 35, 'stock': True},
      {'title': 'Reloj', 'price': 15, 'stock': True}
    ]
  } )

def provincias(request):
  return ()
