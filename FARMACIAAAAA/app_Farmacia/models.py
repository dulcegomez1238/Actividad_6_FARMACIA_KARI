from django.db import models

# ==========================================
# MODELO: PROVEEDOR
# ==========================================
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    rfc = models.CharField(max_length=13)
    fecha_registro = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: PRODUCTO (para la segunda parte)
# ==========================================
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=50)
    fecha_caducidad = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')
    
    def __str__(self):
        return f"{self.nombre} - {self.tipo_producto}"

# ==========================================
# MODELO: INVENTARIO (para la tercera parte)
# ==========================================
class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='inventarios')
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='productos/', blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='inventarios')
    fecha_caducidad = models.DateField()
    contenido = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=0)
    ubicacion = models.CharField(max_length=50, default="Almacén Principal")
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
