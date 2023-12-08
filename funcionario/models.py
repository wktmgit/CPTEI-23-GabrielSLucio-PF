from django.db import models

class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome do funcionário', blank=False)
    cpf = models.CharField('CPF', max_length=15, help_text='CPF do funcionário', unique=True, blank=False)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome