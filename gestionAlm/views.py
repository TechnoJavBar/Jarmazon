from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin #No permite acceder si no se está logeado solo para vistas basadas en clases
from django.contrib.auth import logout

from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, View
from django.urls import reverse_lazy
from .forms import *
from .models import *

from django.contrib import messages

# Create your views here.


def confirmacion(request, pk):
    producto= get_object_or_404(Producto,pk=pk)
    return render(request,'gestionAlm/gestion/confirmacion.html',{'producto':producto})

def login(request):
    return render('gestionAlm/registration/login.html')

def logouthtml(request):
    logout(request)
    return redirect(request,'gestionAlm/registration/logged_out.html')

#! TIENDA
class Index(ListView):
    model= Producto
    form_class=ProductoForm
    template_name='gestionAlm/tienda/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimosCincoProductos'] = Producto.objects.all().order_by('-id').only('titulo', 'imagen')[:5]
        return context


class ListaTienda(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'gestionAlm/tienda/tienda.html'
    context_object_name = 'productos'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

    def get_queryset(self):
        query = super().get_queryset().order_by('precio')

        filtro_nombre = self.request.GET.get('filtro_nombre', '').strip()
        filtro_categoria = self.request.GET.get('filtro_categoria', '').strip()

        if filtro_nombre:
            query = query.filter(titulo__icontains=filtro_nombre)

        if filtro_categoria:
            query = query.filter(categoria__nombre__iexact=filtro_categoria)

        return query



class ComprarDetalle(DetailView):
    model = Producto
    template_name = 'gestionAlm/tienda/comprar_detalle.html'


class Contactos(CreateView):
    model = MensajeContacto
    form_class = MensajeContactoForm
    template_name = 'gestionAlm/tienda/contacto.html'
    success_url = reverse_lazy('contacto')

class ContactosView(LoginRequiredMixin,ListView):
    model = MensajeContacto
    template_name = 'gestionAlm/tienda/contactosListado.html'
    context_object_name = 'mensajes'
    

#! CRUD PRODUCTO

class RegistroProducto(LoginRequiredMixin,CreateView):
    model= Producto
    form_class=ProductoForm
    template_name='registration/registro_producto.html'
    success_url=reverse_lazy('listado')

    def form_valid(self, form):
        messages.success(self.request,'Se ha registrado correctamente')
        form.save()
        return super().form_valid(form)

class ProductoModificado(LoginRequiredMixin,UpdateView):
    model = Producto
    template_name='gestionAlm/gestion/producto_modificado.html'
    fields="__all__"
    success_url=reverse_lazy('listado')

class ProductoBorrar(LoginRequiredMixin,DeleteView):
    model = Producto
    success_url= reverse_lazy('listado')

class ProductoDetalle(LoginRequiredMixin,DetailView):
    model = Producto
    template_name= 'gestionAlm/gestion/producto_detalle.html'
    
    
class ListadoGestion(LoginRequiredMixin,ListView):
    model= Producto
    template_name= 'gestionAlm/gestion/listado.html'
    context_object_name='lista_productos'
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
    
    def get_queryset(self):
        query = super().get_queryset().order_by('precio')

        filtro_nombre = self.request.GET.get('filtro_nombre', '').strip()
        filtro_categoria = self.request.GET.get('filtro_categoria', '').strip()

        if filtro_nombre:
            query = query.filter(titulo__icontains=filtro_nombre)

        if filtro_categoria:
            query = query.filter(categoria__nombre__iexact=filtro_categoria)

        return query    


#! CRUD CATEGORIA

class RegistraCategoria(LoginRequiredMixin,CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'registration/registro_categoria.html'
    success_url = reverse_lazy('listado_categorias')

class CategoriaBorrar(LoginRequiredMixin,DeleteView):
    model = Categoria
    success_url = reverse_lazy('listado')

class ListadoCategorias(LoginRequiredMixin,ListView):
    model = Categoria
    template_name = 'gestionAlm/gestion/categoria_listado.html'
    context_object_name = 'lista_categorias'
    paginate_by = 7


#! CRUD USUARIO
class RegistroView(CreateView):
    model= Usuario
    form_class=UsuarioCreationForm
    template_name='registration/registro.html'
    success_url=reverse_lazy('login')
       

class UsuarioModificado(LoginRequiredMixin,UpdateView):
    model= Usuario
    form_class= UserEditForm
    template_name='users/usuario_modificado.html'
    success_url= reverse_lazy('index')

class UsuarioDetalles(LoginRequiredMixin,DetailView):
    model= Usuario
    template_name="users/usuario_detalles.html"

class UsuarioBorrar(LoginRequiredMixin,DeleteView):
    model= Usuario
    success_url= reverse_lazy('login')


#! COMPRA

class CompraProducto(LoginRequiredMixin,View):
    
    def get(self,request,pk):
        
        producto = get_object_or_404(Producto, pk = pk) # Recojo el producto o lanza error si no lo encuentra
        unidades = int(request.GET.get('unidades')) # Recojo las unidades que el cliente quiere co.mprar
        pvpTotal = producto.precio * int(unidades) # calculo el total de la compra

        return render(request,'gestionAlm/tienda/confirmarCompra.html',{'producto': producto, 'unidades':unidades, 'pvpTotal':pvpTotal})
    
    def post(self, request, pk):

        producto = get_object_or_404(Producto, pk = pk) # Recojo el producto o lanza error si no lo encuentra
        unidades = int(request.POST.get('unidades')) # recojo las unidades que el cliente quiere comprar
        usuario = request.user # obtengo el usuario que realiza la com`pra
        pvpTotal = producto.precio * int(unidades) # calculo el total de la compra

        if unidades <= producto.uds: #comprueba que haya mas stock de los que se com`pra
            Pedido.objects.create(producto=producto, cantidad = int(unidades), pvpTotal = pvpTotal, usuario = usuario) # creo la compra del usuario

            producto.uds -= unidades
            producto.save()
            messages.success(request, 'compra realizada con exito')
        else:
            messages.error(request,'No hay suficiente stock {{producto.uds}}')

        return redirect('tienda')

class ComprasUsuario(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = 'gestionAlm/tienda/compras.html'
    context_object_name = 'compras'

    def get_queryset(self):
        query = super().get_queryset().order_by('fecha')
        query = query.filter(usuario=self.request.user)

        return query
