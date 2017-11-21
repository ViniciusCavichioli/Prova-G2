# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 00:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0002_auto_20171120_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleicao',
            name='eleitor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eleitorEleicao', to='evento.Eleitor'),
        ),
        migrations.RemoveField(
            model_name='vaga',
            name='candidato',
        ),
        migrations.AddField(
            model_name='vaga',
            name='candidato',
            field=models.ManyToManyField(null=True, related_name='candidatoVaga', to='evento.Candidato'),
        ),
    ]