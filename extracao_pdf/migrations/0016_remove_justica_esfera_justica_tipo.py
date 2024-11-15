# Generated by Django 4.1 on 2024-03-29 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extracao_pdf', '0015_alter_processo_arquivo_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='justica',
            name='esfera',
        ),
        migrations.AddField(
            model_name='justica',
            name='tipo',
            field=models.CharField(choices=[('justica_estadual', 'Justiça Estadual'), ('justica_federal', 'Justiça Federal'), ('justica_trabalho', 'Justiça do Trabalho')], default='justica_estadual', max_length=50),
            preserve_default=False,
        ),
    ]