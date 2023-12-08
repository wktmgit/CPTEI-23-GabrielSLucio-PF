from django.db import models

class Chave(models.Model):

    #  PUXAR AS COLUNAS DA SALA PARA A TABELA ATUAL DAS CHAVES
    sala = models.ForeignKey('sala.Sala', verbose_name='Sala', on_delete=models.PROTECT)

    DISPONIVEL = 'Disponível'
    OCUPADA = 'Ocupada'

    DISPONIBILIDADE_CHAVE = [
        (DISPONIVEL, 'Disponível'),
        (OCUPADA, 'Ocupada'),
    ]

    codigo = models.CharField('Código', max_length=50, help_text='Código da chave', unique=True,)
    disponibilidade = models.CharField('Disponibilidade da sala', max_length=10, choices=DISPONIBILIDADE_CHAVE, blank=False, null=False, default=DISPONIVEL,)


    class Meta:
        verbose_name = 'Chave'
        verbose_name_plural = 'Chaves'

    def __str__(self):
        return f'{self.codigo} - {self.sala}'