from django.db import models
from django.contrib.auth.models import AbstractUser

# ! Create your models here.
class Producto(models.Model):
    titulo= models.CharField(max_length=100, unique=True, blank=False)
    descripcion= models.TextField(max_length=200)
    precio= models.DecimalField(decimal_places=2 , max_digits=5, blank=False)
    uds= models.IntegerField(blank=False)
    imagen = models.ImageField(upload_to='imagenes/producto')
    dimensiones = models.DecimalField(decimal_places=2, max_digits=5)
    cantidad = models.CharField(max_length=30)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.titulo} -- {self.precio}€")

class Categoria(models.Model):
    nombre= models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return (f"{self.nombre}")

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

class Usuario(AbstractUser):
    direccion= models.CharField(max_length=100, verbose_name='Direccion',blank=True)
    imagen = models.ImageField(upload_to='imagenes/usuario')
    

    def __str__(self):
        return (f"{self.username} {self.email}")
    
    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'

    
class Pedido(models.Model):
    producto = models.ForeignKey(Producto, verbose_name=("producto"), on_delete=models.CASCADE)
    cantidad = models.IntegerField(blank=False)
    fecha= models.DateField(auto_now_add=True)
    usuario= models.ForeignKey(Usuario, verbose_name=("usuario"), on_delete=models.CASCADE)
    pvpTotal = models.IntegerField()

    def __str__(self):
        return (f"{self.producto} -- {self.usuario} -- {self.fecha}")

    class Meta:
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        unique_together = ['producto', 'usuario', 'fecha']


class MensajeContacto(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    mensaje= models.TextField(max_length=1000)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='mensajeContacto'
        verbose_name_plural='mensajesContactos'

    def __str__(self):
        return (f"{self.email} -- {self.nombre} -- {self.fecha}")