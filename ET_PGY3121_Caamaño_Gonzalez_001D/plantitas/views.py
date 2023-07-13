from django.shortcuts import render, redirect
from .forms import ProductosForm, RegistroUserForm
from .models import Boleta, Producto ,detalle_boleta
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from plantitas.compra import Carrito


# Create your views here.
def inicio(request):
    return render(request,'inicio.html')


def pagina2(request):
    return render(request,'pagina2.html')

def formulario(request):
    return render(request,'formulario.html')


def api(request):
    return render(request,'api.html')


def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado Exitosamente []~(￣▽￣)~*")
            return redirect ('index')
        data["form"] = formulario
    return render(request, 'registration/registrar.html',data)




@login_required
def crear(request):
    if request.method=="POST":
        productosform = ProductosForm(request.POST, request.FILES)
        if productosform.is_valid():
            productosform.save()     #similar al insert
            return redirect('pagina3')
    else:
        productosform=ProductosForm()
    return render(request, 'crear.html', {'productosform':productosform})


@login_required
def eliminar(request, id):
    productoEliminado = Producto.objects.get(id=id) 
    productoEliminado.delete()
    return redirect ('pagina3')


@login_required
def modificar(request, idproducto):
    producto = Producto.objects.get(id=idproducto)
    datos = {
        'form': ProductosForm(instance=producto)
    }
    if request.method=='POST':
        formulario = ProductosForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            instance = formulario.save(commit=False)
            if 'imagen' in request.FILES:
                instance.imagen = request.FILES['imagen']
                instance.save()
            return redirect('pagina3')
    return render(request, 'modificar.html', datos)





def tienda(request):
    producto = Producto.objects.all()
    datos={
        'productos':producto
    }
    return render(request, 'pagina3.html', datos)


def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito_compra.agregar(producto=producto)
    return redirect('pagina3')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('pagina3')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito_compra.restar(producto=producto)
    return redirect('pagina3')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('pagina3')    


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(id = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)

