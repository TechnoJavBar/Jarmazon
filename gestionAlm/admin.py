from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Producto,Usuario, Categoria


class CustomUserAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
         (None, {'fields': ('direccion','meta')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
         (None, {'fields': ('direccion', 'meta')}),
    )



# Register your models here.
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Categoria)