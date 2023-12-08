from django.db import models
from django.utils.timezone import now

import retirada
from chave.models import Chave


class Retirada(models.Model):

    STATUS = (
        ("Retirada", "Retirada"),
        ("Devolvida", "Devolvida"),
        ("Atrasada", "Atrasada")
    )

    sala = models.ForeignKey('sala.Sala', verbose_name='Sala', on_delete=models.PROTECT)
    chave = models.ForeignKey('chave.Chave', verbose_name='Chave', on_delete=models.PROTECT)

    dataretirada = models.DateTimeField('data_retirada', help_text='Data da retirada chave', blank=False, default=now)
    datadevolucao = models.DateTimeField('data_devolucao', help_text='Data da devolução da chave', blank=False, default=now)

    status = models.CharField('estatus', max_length=20, help_text='Estatus da retirada', choices=STATUS, default='Retirada')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        chave = Chave.objects.get(pk=self.chave.pk)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)


    def delete(self, using=None, keep_parents=False):
        super().delete(using=None, keep_parents=False)

    class Meta:
        verbose_name = 'Retirada'
        verbose_name_plural = 'Retiradas'

    def __str__(self):
        return f'{self.sala} - {self.chave} - {self.dataretirada}'