from django import forms
from .models import Atleta, Entrenador, Biblioteca,Clase,Reserva


class AtletaForm(forms.ModelForm):
    class Meta:
        model = Atleta
        fields = ['nombre', 'apellido', 'email','plan']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'plan': forms.Select(attrs={'class': 'form-select'}),
        }

class EntrenadorForm(forms.ModelForm):
    class Meta: 
        model = Entrenador
        fields = ['nombre', 'apellido','especialidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'especialidad': forms.Select(attrs={'class':'form-select'}),
        }

class BibliotecaForm(forms.ModelForm):
    class Meta:
        model = Biblioteca
        fields = ['nombre', 'descripcion', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del ejercicio'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción del ejercicio'
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'imagen': 'Imagen del ejercicio'
        }
#aca pongo reservas
class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['nombre', 'horario', 'fecha', 'entrenador', 'capacidad_maxima']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'horario': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'entrenador': forms.Select(attrs={'class': 'form-select'}),
            'capacidad_maxima': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['atleta', 'clase']
        widgets = {
            'atleta': forms.Select(attrs={'class': 'form-select'}),
            'clase': forms.Select(attrs={'class': 'form-select'}),
        }