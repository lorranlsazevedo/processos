# Generated by Django 4.1 on 2024-04-09 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extracao_pdf', '0022_remove_processo_conteudo_texto_rico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='bairro',
            field=models.CharField(blank=True, max_length=100, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='cep',
            field=models.CharField(blank=True, max_length=9, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='cidade',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='extracao_pdf.cidade', verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='numero',
            field=models.CharField(blank=True, max_length=10, verbose_name='Número do Endereço'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='rua',
            field=models.CharField(blank=True, max_length=255, verbose_name='Rua'),
        ),
    ]
