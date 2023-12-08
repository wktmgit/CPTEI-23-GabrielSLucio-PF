from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from chave.forms import ChaveModelForm
from chave.models import Chave


class ChavesView(ListView):
    model = Chave
    template_name = 'chaves.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ChavesView, self).get_queryset()
        if buscar:
            qs = qs.filter(codigo__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem chaves cadastradas!")


class ChaveAddView(SuccessMessageMixin, CreateView):
    form_class = ChaveModelForm
    model = Chave
    template_name = 'chave_form.html'
    success_url = reverse_lazy('chaves')
    success_message = 'Chave cadastrada com sucesso!'


class ChaveUpDateView(SuccessMessageMixin, UpdateView):
    form_class = ChaveModelForm
    model = Chave
    template_name = 'chave_form.html'
    success_url = reverse_lazy('chaves')
    success_message = 'Chave alterada com sucesso!'


class ChaveDeleteView(SuccessMessageMixin, DeleteView):
    model = Chave
    template_name = 'chave_apagar.html'
    success_url = reverse_lazy('chaves')
    success_message = 'Chave apagada com sucesso!'
