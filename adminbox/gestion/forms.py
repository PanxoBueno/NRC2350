from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Entrenador, Atleta, Clase, Reserva

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = ['especialidad', 'telefono']

class AtletaForm(forms.ModelForm):
    class Meta:
        model = Atleta
        fields = ['fecha_nacimiento', 'telefono', 'entrenador']

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['nombre', 'descripcion', 'horario', 'capacidad', 'entrenador']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['clase']