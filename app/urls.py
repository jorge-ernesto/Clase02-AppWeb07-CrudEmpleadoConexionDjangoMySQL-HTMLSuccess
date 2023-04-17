from django.urls import path
from . import views

urlpatterns = [
    path(''                  , views.listarempleado   , name='listarempleado'),
    path('insertar/'         , views.insertarempleado , name='insertarempleado'),
    path('editar/<int:id>'   , views.editarempleado   , name='editarempleado'),
    path('modificar/<int:id>', views.modificarempleado, name='modificarempleado'),
    path('eliminar/<int:id>' , views.eliminarempleado , name='eliminarempleado'),
]
