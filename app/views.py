from django.shortcuts import render
from .models import Empleado
from django.db import connection  # Usamos conexion de Django
from django.contrib import messages

# Create your views here.

def listarempleado(request):
    #abrir conexion a la BD
    cursor = connection.cursor()
    #ejecutar comando del sql
    cursor.execute('select * from empleado')
    empleados = cursor.fetchall()
    return render(request,'app/index.html',{'empleados':empleados})

def insertarempleado(request):
    if request.method == 'POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('email'):
            #crear objeto de la clase empleado
            emp = Empleado()
            #asignar valores al objeto emp
            emp.nombre = request.POST.get('nombre')
            emp.apellido = request.POST.get('apellido')
            emp.email = request.POST.get('email')
            # abrir conexion a BD
            cursor = connection.cursor()
            #ejecutar comando insert
            cursor.execute('insert into empleado(nombre,apellido,email,estado) values(%s,%s,%s,%s)',(emp.nombre,emp.apellido,emp.email,1))
            messages.success(request,'Empleado registrado con exito!')
            return render(request,'app/add.html')
    else:
        return render(request,'app/add.html')
    
def editarempleado(request,id):
    cursor = connection.cursor()
    cursor.execute('select * from empleado where id = %s',(id,))
    empleado = cursor.fetchone()
    contexto = {'empleado':empleado}
    return render(request,'app/editar.html',contexto)

def modificarempleado(request,id):
    if request.method == 'POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('email'):
            #crear objeto de la clase empleado
            emp = Empleado()
            #asignar valores al objeto emp
            emp.id = id
            emp.nombre = request.POST.get('nombre')
            emp.apellido = request.POST.get('apellido')
            emp.email = request.POST.get('email')
            # abrir conexion a BD
            cursor = connection.cursor()
            #ejecutar comando update
            cursor.execute('update empleado set nombre = %s,apellido = %s,email = %s where id = %s',(emp.nombre,emp.apellido,emp.email,emp.id))
            messages.success(request,'Empleado actualizado con exito!')
            return render(request,'app/editar.html')
    else:
        return render(request,'app/editar.html') 
    
def eliminarempleado(request,id):
    cursor = connection.cursor()
    cursor.execute('delete from empleado where id = %s',(id,))
    cursor = connection.cursor()
    cursor.execute('select * from empleado')
    empleados = cursor.fetchall()
    contexto = {'empleados':empleados}
    return render(request,'app/index.html',contexto)
