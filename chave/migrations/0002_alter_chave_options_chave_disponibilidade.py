# Generated by Django 4.2.5 on 2023-12-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chave', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chave',
            options={'verbose_name': 'Chave', 'verbose_name_plural': 'Chaves'},
        ),
        migrations.AddField(
            model_name='chave',
            name='disponibilidade',
            field=models.CharField(choices=[('Disponível', 'Disponível'), ('Ocupada', 'Ocupada')], default='Disponível', max_length=10, verbose_name='Disnibilidade da sala'),
        ),
    ]
