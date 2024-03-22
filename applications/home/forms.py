from django import forms

#importar modelo Prueba 
from .models import Prueba

class PruebaForm(forms.ModelForm):
  """Form definition for PruebaForm."""

  class Meta:
    """Meta definition for MODELNAMEform."""
    model = Prueba
    fields = (
      'titulo',
      'subtitulo',
      'cantidad',
    )

  def clean_cantidad(self):
      cantidad = self.cleaned_data['cantidad']
      if cantidad < 10:
          raise forms.ValidationError('Ingrese un numero menor a 10')
      return cantidad  
    


