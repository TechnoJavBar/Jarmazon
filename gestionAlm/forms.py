from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import EmailValidator, MinLengthValidator
from django.contrib.auth import get_user_model
from .models import Usuario, Producto, MensajeContacto, Categoria
from django.core.exceptions import ValidationError

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # Esto asegura que use tu modelo personalizado
        fields = ['username', 'email', 'first_name', 'last_name','direccion','imagen']  # Ajusta los campos según tu modelo

class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'username', 'direccion', 'imagen']

class ProductoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all()) #! Esto permite seleccionar la categoria de las existentes

    class Meta:
        model = Producto
        fields= '__all__' #! Aqui esta incluida ya la categoia de arriba
        
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.all()

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields= '__all__'
        
class MensajeContactoForm(forms.ModelForm):
    class Meta:
        model= MensajeContacto
        fields = '__all__'