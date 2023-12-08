from django import forms

from .models import Sala

class SalaModelForm(forms.ModelForm):

    class Meta:
        model = Sala
        fields = ['identificacao','tipo']

    error_messages = {
        'identificacao': {'required': 'A idenficação da sala é obrigatória', 'unique': 'Identificação já cadastrada'},
        'tipo': {'required': 'O tipo da sala é obrigatório'},
    }