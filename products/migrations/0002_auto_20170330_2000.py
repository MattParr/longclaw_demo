# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='description',
        ),
        migrations.AddField(
            model_name='productvariant',
            name='size',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default='S', max_length=3),
            preserve_default=False,
        ),
    ]
