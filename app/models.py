from django.db import models

# Create your models here.

class Empleado(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'empleado'  # Especificar el nombre de la tabla que se creara en la migración
