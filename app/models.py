from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=40)
    email=models.EmailField(max_length=100)
    estado=models.BooleanField(default=True)


    class Meta:
        db_table='empleado'
        