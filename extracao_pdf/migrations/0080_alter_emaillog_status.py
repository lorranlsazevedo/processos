# Generated by Django 4.1 on 2024-08-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extracao_pdf', '0079_processo_venda_direta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaillog',
            name='status',
            field=models.CharField(choices=[('pending', 'Pendente'), ('sent', 'Enviado'), ('failed', 'Falhou')], default='pending', max_length=10),
        ),
    ]
