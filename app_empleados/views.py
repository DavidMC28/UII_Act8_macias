

# Create your views here.
# app_editoriales/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado

# Listar editoriales (READ)
def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'listar_empleados.html', {'empleados': empleados})

# Agregar editorial (CREATE)
def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST.get('direccion', '') # .get() para campos opcionales
        telefono = request.POST.get('telefono', '')
        email = request.POST.get('email', '')
        pais_origen = request.POST.get('pais_origen', '')

        Empleado.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            pais_origen=pais_origen
        )
        return redirect('listar_editoriales')
    return render(request, 'agregar_editorial.html')

# Editar editorial (UPDATE)
def editar_empleado(request, pk): # 'pk' (Primary Key) es el 'id' de la editorial
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.direccion = request.POST.get('direccion', '')
        empleado.telefono = request.POST.get('telefono', '')
        empleado.email = request.POST.get('email', '')
        empleado.pais_origen = request.POST.get('pais_origen', '')
        empleado.save()
        return redirect('listar_empledos')
    return render(request, 'editar_empleado.html', {'empleado': empleado})

# Borrar editorial (DELETE)
def borrar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('listar_empleados')
    return render(request, 'borrar_empleado.html', {'empleado': empleado})