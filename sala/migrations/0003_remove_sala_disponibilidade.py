# Generated by Django 4.2.5 on 2023-12-06 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sala', '0002_sala_disponibilidade_alter_sala_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sala',
            name='disponibilidade',
        ),
    ]