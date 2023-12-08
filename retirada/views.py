from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

import retirada
from chave.models import Chave
from retirada.forms import RetiradaModelForm
from retirada.models import Retirada


class RetiradasView(ListView):
    model = Retirada
    template_name = 'retiradas.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(RetiradasView, self).get_queryset()
        for retirada in qs:
            if retirada.status == 'Retirada' or 'Expirada':
                chave = retirada.chave
                chave.disponibilidade = 'Ocupada'
                chave.save()
        if buscar:
            qs = qs.filter(codigo__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem retiradas cadastradas!")


class DevolucaoView(DetailView):
    model = Retirada
    template_name = 'retirada_devolucao.html'
    context_object_name = 'retirada'
    pk_url_kwarg = 'retirada_id'

    def post(self, request, *args, **kwargs):
        retirada = self.get_object()
        retirada.data_devolucao = timezone.now()
        retirada.save()
        return redirect('retiradas')

    # def get_object(self, queryset=None):
    #     retirada = Retirada.objects.get(pk=self.kwargs.get('pk'))
    #     if retirada.status == 'Retirada' or 'Expirada':
    #         chave = retirada.chave
    #
    #         if retirada.datadevolucao < timezone.now():
    #             chave.disponibilidade = 'Disponível'
    #             chave.save()
    #             retirada.status = 'Devolvida'
    #             retirada.save()
    #         else:
    #             retirada.status = 'Expirada'
    #             retirada.save()
    #
    #     return retirada


class RetiradaAddView(SuccessMessageMixin, CreateView):
    form_class = RetiradaModelForm
    model = Retirada
    template_name = 'retirada_form.html'
    success_url = reverse_lazy('retiradas')
    success_message = 'Retirada cadastrada com sucesso!'


class RetiradaUpDateView(SuccessMessageMixin, UpdateView):
    form_class = RetiradaModelForm
    model = Retirada
    template_name = 'retirada_form.html'
    success_url = reverse_lazy('retiradas')
    success_message = 'Retirada alterada com sucesso!'


class RetiradaDeleteView(SuccessMessageMixin, DeleteView):
    model = Retirada
    template_name = 'retirada_apagar.html'
    success_url = reverse_lazy('retiradas')
    success_message = 'Retirada apagada com sucesso!'
