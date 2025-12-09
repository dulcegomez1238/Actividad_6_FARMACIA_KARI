from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_Farmacia, name='inicio'),
    
    # Proveedor URLs
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedor/actualizar/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/borrar/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),


    # Producto URLs
path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
path('producto/', views.ver_productos, name='ver_productos'),
path('producto/actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
path('producto/borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),



# Inventario URLs
path('inventario/agregar/', views.agregar_inventario, name='agregar_inventario'),
path('inventario/', views.ver_inventarios, name='ver_inventarios'),
path('inventario/actualizar/<int:id>/', views.actualizar_inventario, name='actualizar_inventario'),
path('inventario/borrar/<int:id>/', views.borrar_inventario, name='borrar_inventario'),
]