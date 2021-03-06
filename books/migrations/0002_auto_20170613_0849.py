# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 00:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '\u8457\u4f5c\u8005\u8868', 'verbose_name_plural': '\u8457\u4f5c\u8005\u8868'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '\u4e66\u7c4d\u8868', 'verbose_name_plural': '\u4e66\u7c4d\u8868'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name'], 'verbose_name': '\u51fa\u7248\u793e\u8868', 'verbose_name_plural': '\u51fa\u7248\u793e\u8868'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher_date',
        ),
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.DateField(blank=True, null=True, verbose_name='\u51fa\u7248\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='\u540d\u5b57'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name='\u59d3\u6c0f'),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='books.Author', verbose_name='\u4f5c\u8005'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Publisher', verbose_name='\u51fa\u7248\u673a\u6784'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u4e66\u540d'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.CharField(max_length=50, verbose_name='\u6240\u5728\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='city',
            field=models.CharField(max_length=60, verbose_name='\u6240\u5728\u57ce\u5e02'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(max_length=50, verbose_name='\u6240\u5728\u56fd\u5bb6'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=30, verbose_name='\u51fa\u7248\u793e'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='state_province',
            field=models.CharField(max_length=30, verbose_name='\u6240\u5728\u7701\u4efd'),
        ),
    ]
