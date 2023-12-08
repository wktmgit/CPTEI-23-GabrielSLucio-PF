from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from sala.forms import SalaModelForm
from sala.models import Sala

class SalasView(ListView):
    model = Sala
    template_name = 'salas.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(SalasView, self).get_queryset()
        if buscar:
            qs = qs.filter(identificacao__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem salas cadastradas!")

class SalaAddView(SuccessMessageMixin, CreateView):
    form_class = SalaModelForm
    model = Sala
    template_name = 'sala_form.html'
    success_url = reverse_lazy('salas')
    success_message = 'Sala cadastrada com sucesso!'

class SalaUpDateView(SuccessMessageMixin, UpdateView):
    form_class = SalaModelForm
    model = Sala
    template_name = 'sala_form.html'
    success_url = reverse_lazy('salas')
    success_message = 'Sala alterada com sucesso!'

class SalaDeleteView(SuccessMessageMixin, DeleteView):
    model = Sala
    template_name = 'sala_apagar.html'
    success_url = reverse_lazy('salas')
    success_message = 'Sala apagada com sucesso!'