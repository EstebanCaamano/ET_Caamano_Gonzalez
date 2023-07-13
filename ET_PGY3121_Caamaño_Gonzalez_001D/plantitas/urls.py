from django.urls import path
from .views import *
urlpatterns=[ 
    path('', inicio, name="inicio"),
    path('pagina2/', pagina2, name="pagina2"),
    path('pagina3/',tienda,name="pagina3"),
    path('formulario/',formulario , name="formulario"),    
    path('api/',api , name="api"),
    path('registrar/',registrar,name="registrar"),
    path('crear/',crear,name="crear"),
    path('modificar/<idproducto>',modificar,name="modificar"),
    path('eliminar/<id>',eliminar, name="eliminar"),

    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),

    
    

]


