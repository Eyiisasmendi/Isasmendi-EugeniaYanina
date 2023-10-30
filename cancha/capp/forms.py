from django import forms
from .models import Cancha, CategoriaCancha, Cliente, Reserva
from ckeditor.widgets import CKEditorWidget

#Formulario de Registro de Categoría de Cancha:
class CategoriaCanchaForm(forms.ModelForm):
    class Meta:
        model = CategoriaCancha
        fields = ['nombre', 'img_cancha', 'categoria']

#Formulario de Registro de Cancha:
class CanchaForm(forms.ModelForm):
    class Meta:
        model = Cancha
        fields = ['nombre', 'cancha_id']

#Formulario de Registro de Cliente:
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'teléfono_celular', 'correo_electrónico', 'socio']

#Formulario de Registro de Reserva:
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'cliente_id', 'cancha_id', 'estado', 'precio', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la reserva'}),
            'cliente_id': forms.Select(attrs={'class': 'form-control'}),
            'cancha_id': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'descripcion': CKEditorWidget(),
        }

    labels = {
            'nombre': "",
            
        }