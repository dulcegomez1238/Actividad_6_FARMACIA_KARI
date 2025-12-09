from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Producto, Inventario

# ==========================================
# VISTAS PARA PROVEEDOR
# ==========================================

def inicio_Farmacia(request):
    return render(request, 'inicio.html')

def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        rfc = request.POST.get('rfc')
        
        Proveedor.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            rfc=rfc
        )
        return redirect('ver_proveedores')
    
    return render(request, 'proveedor/agregar_proveedor.html')

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.rfc = request.POST.get('rfc')
        proveedor.save()
        return redirect('ver_proveedores')
    
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})




# ==========================================
# VISTAS PARA PRODUCTO
# ==========================================

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo_producto = request.POST.get('tipo_producto')
        fecha_caducidad = request.POST.get('fecha_caducidad')
        precio = request.POST.get('precio')
        proveedor_id = request.POST.get('proveedor')
        
        proveedor = get_object_or_404(Proveedor, id=proveedor_id)
        
        Producto.objects.create(
            nombre=nombre,
            tipo_producto=tipo_producto,
            fecha_caducidad=fecha_caducidad,
            precio=precio,
            proveedor=proveedor
        )
        return redirect('ver_productos')
    
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/agregar_producto.html', {'proveedores': proveedores})

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.tipo_producto = request.POST.get('tipo_producto')
        producto.fecha_caducidad = request.POST.get('fecha_caducidad')
        producto.precio = request.POST.get('precio')
        proveedor_id = request.POST.get('proveedor')
        
        if proveedor_id:
            producto.proveedor = get_object_or_404(Proveedor, id=proveedor_id)
        
        producto.save()
        return redirect('ver_productos')
    
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/actualizar_producto.html', {
        'producto': producto,
        'proveedores': proveedores
    })

def realizar_actualizacion_producto(request):
    # Esta función manejará la actualización (similar a actualizar_producto)
    pass

def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    
    return render(request, 'producto/borrar_producto.html', {'producto': producto})






# ==========================================
# VISTAS PARA INVENTARIO
# ==========================================

def agregar_inventario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        fecha_caducidad = request.POST.get('fecha_caducidad')
        contenido = request.POST.get('contenido')
        cantidad = request.POST.get('cantidad')
        ubicacion = request.POST.get('ubicacion')
        producto_id = request.POST.get('producto')
        proveedor_id = request.POST.get('proveedor')
        
        producto = get_object_or_404(Producto, id=producto_id)
        proveedor = get_object_or_404(Proveedor, id=proveedor_id)
        
        Inventario.objects.create(
            nombre=nombre,
            tipo=tipo,
            fecha_caducidad=fecha_caducidad,
            contenido=contenido,
            cantidad=cantidad,
            ubicacion=ubicacion,
            producto=producto,
            proveedor=proveedor
        )
        return redirect('ver_inventarios')
    
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, 'inventario/agregar_inventario.html', {
        'productos': productos,
        'proveedores': proveedores
    })

def ver_inventarios(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inventario/ver_inventarios.html', {'inventarios': inventarios})

def actualizar_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    
    if request.method == 'POST':
        inventario.nombre = request.POST.get('nombre')
        inventario.tipo = request.POST.get('tipo')
        inventario.fecha_caducidad = request.POST.get('fecha_caducidad')
        inventario.contenido = request.POST.get('contenido')
        inventario.cantidad = request.POST.get('cantidad')
        inventario.ubicacion = request.POST.get('ubicacion')
        
        producto_id = request.POST.get('producto')
        proveedor_id = request.POST.get('proveedor')
        
        if producto_id:
            inventario.producto = get_object_or_404(Producto, id=producto_id)
        if proveedor_id:
            inventario.proveedor = get_object_or_404(Proveedor, id=proveedor_id)
        
        inventario.save()
        return redirect('ver_inventarios')
    
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, 'inventario/actualizar_inventario.html', {
        'inventario': inventario,
        'productos': productos,
        'proveedores': proveedores
    })

def borrar_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    
    if request.method == 'POST':
        inventario.delete()
        return redirect('ver_inventarios')
    
    return render(request, 'inventario/borrar_inventario.html', {'inventario': inventario})