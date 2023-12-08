from django import forms

from sala.models import Sala
from chave.models import Chave
from .models import Retirada

class RetiradaModelForm(forms.ModelForm):

    sala = forms.ModelChoiceField(label='Sala:', widget=forms.Select(attrs={'class': 'select is-fullwidth'}), queryset=Sala.objects.all(), required=False)
    chave = forms.ModelChoiceField(label='Chave:', widget=forms.Select(attrs={'class': 'select is-fullwidth'}),
                                  queryset=Chave.objects.all(), required=False)
    class Meta:
        model = Retirada
        fields = ['sala', 'chave', 'dataretirada', 'datadevolucao']

    error_messages = {
        'sala': {'required': 'A sala é obrigatória'},
        'chave': {'required': 'A chave é obrigatória'},
        'dataretirada': {'required': 'A data da retirada é obrigatória'},
        'datadevolucao': {'required': 'A data da devolução é obrigatória'}
    }