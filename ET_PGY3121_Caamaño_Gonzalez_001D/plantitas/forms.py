from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Producto
from django.forms.models import ModelChoiceField



class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields =['id','nombre','imagen','precio','categoria','stock']
        labels ={
            'id':'Id',
            'nombre':'Nombre',
            'imagen':'Imagen',
            'precio':'Precio',
            'categoria':'Categoria',
            'stock':'Stock'
        }
        widgets ={
            'id' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingresar numero identificador',
                    'id':'id',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingresar nombre del producto',
                    'id':'nombre',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingresar imagen',
                    'id':'imagen',
                }
            ),
            'precio':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingresar precio del producto',
                    'id':'precio',
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingresar categoria',
                    'id':'categoria',
                }
            ),
            'stock':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingresar cantidad de stock',
                    'id':'stock',
                }
            ),
        }
