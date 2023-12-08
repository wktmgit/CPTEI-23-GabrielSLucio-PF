from django import forms

from sala.models import Sala
from .models import Chave

class ChaveModelForm(forms.ModelForm):

    sala = forms.ModelChoiceField(label='Sala Associada:', help_text='Sala que está associada à chave', widget=forms.Select(attrs={'class': 'select is-fullwidth'}), queryset=Sala.objects.all(), required=False)
    class Meta:
        model = Chave
        fields = ['codigo','disponibilidade','sala']

    error_messages = {
        'codigo': {'required': 'O código da chave é obrigatório', 'unique': 'Código já cadastrado'},
        'disponibilidade': {'required': 'A disponibilidade é obrigatória'},
        'sala': {'required': 'A sala é obrigatória'},
    }