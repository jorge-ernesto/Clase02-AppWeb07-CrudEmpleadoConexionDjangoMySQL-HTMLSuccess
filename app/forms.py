from django import forms
from app.models import Empleado

# El formulario hereda las validaciones definidas en el modelo.
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        # fields = ['nombre', 'apellido', 'email', 'estado']  # Otra forma
