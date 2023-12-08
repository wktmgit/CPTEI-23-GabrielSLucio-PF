# Generated by Django 4.2.5 on 2023-12-04 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do cliente', max_length=50, verbose_name='Nome')),
                ('cpf', models.CharField(help_text='CPF do funcionário', max_length=15, unique=True, verbose_name='CPF')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
    ]
