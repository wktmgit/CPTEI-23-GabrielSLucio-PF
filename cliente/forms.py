from django import forms

from .models import Cliente

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'matricula']

    error_messages = {
        'nome': {'required': 'O nome do cliente é obrigatório'},
        'matricula': {'required': 'A matrícula do cliente é obrigatória', 'unique': 'Matrícula já cadastrada'},
    }