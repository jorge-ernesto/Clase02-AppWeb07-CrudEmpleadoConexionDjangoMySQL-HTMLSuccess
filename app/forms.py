from django import forms
from app.models import Empleado

class EmpleadoForm(forms.ModelForm):

    class meta:
        model=Empleado
        fields='__all__'
        #fields=['nombre','apellido','email','estado']