from django import forms

from .models import Funcionario


class FuncionarioModelForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = ['nome', 'cpf']

    error_messages = {
        'nome': {'required': 'O nome do funcionário é obrigatório'},
        'cpf': {'required': 'O CPF do funcionário é obrigatório', 'unique': 'CPF já cadastrado'},
    }