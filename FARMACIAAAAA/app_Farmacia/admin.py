from django.contrib import admin
from .models import Proveedor, Producto, Inventario

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'rfc', 'activo')
    search_fields = ('nombre', 'rfc')
    list_filter = ('activo',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_producto', 'precio', 'proveedor')
    search_fields = ('nombre', 'tipo_producto')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'cantidad', 'ubicacion')
    search_fields = ('nombre', 'tipo')