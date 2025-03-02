from django.urls import path
from . import views
from .views import *

urlpatterns = [
    
    #! CRUD PRODUCTO
    path('gestion/producto/listado',ListadoGestion.as_view(),name='listado'),
    path('gestion/producto/listado/<int:pk>',ProductoDetalle.as_view(), name='producto_detalle'),
    path('gestion/producto/modificar/<int:pk>',ProductoModificado.as_view(), name='producto_modificado'),
    path('gestion/listado/eliminar/<int:pk>',ProductoBorrar.as_view(), name='producto_borrado'),
    path('gestion/producto/nuevo',RegistroProducto.as_view(),name='Crear_producto'),

    #! CRUD CATEGORIA
    path('gestion/categoria/listado', ListadoCategorias.as_view(), name='listado_categorias'),
    path('gestion/categoria/nuevo',RegistraCategoria.as_view(), name='crear_categoria'),
    path('gestion/categoria/borrar/<int:pk>', CategoriaBorrar.as_view(), name='borrar_categoria'),

    #! LOGIN Y LOGOUT
    path('account/login',views.login,name='login'),
    path("logout/",views.logouthtml, name='logout'),

    #! CRUD USUARIO
    path('registro/',RegistroView.as_view(),name='registro'),
    path('perfil/modificar/<int:pk>',UsuarioModificado.as_view(),name='perfil_modificado'),
    path('perfil/<int:pk>',UsuarioDetalles.as_view(), name='perfil_detalles'),

    #! TIENDA
    path('',Index.as_view(), name='index'),
    path('tienda',ListaTienda.as_view(), name='tienda'),
    path('tienda/<int:pk>',ComprarDetalle.as_view(), name='comprar_detalle'),
    path('tienda/contacto',Contactos.as_view(), name='contacto'),
    path('tienda/confirmarProducto/<int:pk>',CompraProducto.as_view(), name="checkout"),
    path('carrito',ComprasUsuario.as_view(), name="comprasUsuario"),

    path('mensajes/listado',ContactosView.as_view(), name="listadoMensajes"),
]
