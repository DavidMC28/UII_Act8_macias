# app_editoriales/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_empleados, name='listar_empleados'),
    # Las rutas para ver, agregar, editar y borrar usan la ID (pk)
    path('agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('editar/<int:pk>/', views.editar_empleado, name='editar_empleado'),
    path('borrar/<int:pk>/', views.borrar_empleado, name='borrar_empleado'),
]