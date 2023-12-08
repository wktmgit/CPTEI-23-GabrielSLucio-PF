from django.db import models

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome do cliente', blank=False)
    matricula = models.CharField('Matrícula', max_length=15, help_text='Matrícula do cliente', unique=True, blank=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome