from django.db import models

class Sala(models.Model):
    EXCLUSIVA = 'Exclusiva'
    COMUNITARIA = 'Comunitária'

    Tipos = [
        (EXCLUSIVA, 'Exclusiva'),
        (COMUNITARIA, 'Comunitária'),
    ]

    identificacao = models.CharField('Identificação', max_length=50, help_text='Identificação da sala', unique=True,)
    tipo = models.CharField('Tipo da sala', max_length=11, choices=Tipos, blank=False, null=False, default=COMUNITARIA,)

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'

    def __str__(self):
        return f'{self.identificacao} ({self.tipo})'