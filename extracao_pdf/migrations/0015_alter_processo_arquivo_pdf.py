# Generated by Django 4.1 on 2024-03-22 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extracao_pdf', '0014_processo_arquivo_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='arquivo_pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
