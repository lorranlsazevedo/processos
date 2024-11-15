# Generated by Django 4.1 on 2024-03-20 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extracao_pdf', '0012_bem_data_avaliacao_bem_tipo_bem_alter_bem_valor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=20, unique=True, verbose_name='Número da Matrícula')),
                ('rua', models.CharField(max_length=255, verbose_name='Rua')),
                ('numero', models.CharField(max_length=10, verbose_name='Número do Endereço')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extracao_pdf.cidade', verbose_name='Cidade')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extracao_pdf.estado', verbose_name='Estado da Matrícula')),
            ],
        ),
        migrations.CreateModel(
            name='Leiloeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=20)),
                ('site', models.URLField(blank=True)),
                ('matriculas', models.ManyToManyField(to='extracao_pdf.matricula', verbose_name='Matrículas')),
            ],
        ),
        migrations.AddField(
            model_name='processo',
            name='leiloeiro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='extracao_pdf.leiloeiro', verbose_name='Leiloeiro'),
        ),
    ]