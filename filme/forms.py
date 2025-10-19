from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class CriarContaForm(UserCreationForm):
    #Aqui vc adiciona demais campos que quer no formulario padrao do django
    email = forms.EmailField()

    # Aqui diz ao django que ele ira criar um formulari baseado na class Usuario
    class Meta:
        model = Usuario
        # Aqui diz quais campos vc quer mostrar no form inclusive o que vc criou anteriormente EMAIL
        fields = ['username', 'email', 'password1', 'password2']

class FormHome(forms.Form):
    email = forms.EmailField(label=False)
