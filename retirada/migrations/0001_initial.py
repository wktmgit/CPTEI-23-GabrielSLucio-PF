# Generated by Django 4.2.5 on 2023-12-07 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chave', '0005_alter_chave_sala'),
        ('sala', '0003_remove_sala_disponibilidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retirada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataretirada', models.DateField(help_text='Data da retirada chave', verbose_name='data_retirada')),
                ('datadevolucao', models.DateField(help_text='Data da devolução da chave', verbose_name='data_devolucao')),
                ('chave', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chave.chave', verbose_name='Chave')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sala.sala', verbose_name='Sala')),
            ],
            options={
                'verbose_name': 'Retirada',
                'verbose_name_plural': 'Retiradas',
            },
        ),
    ]