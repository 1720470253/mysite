# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='id',
        ),
        migrations.AlterField(
            model_name='author',
            name='AuthorID',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='AuthorID',
            field=models.ForeignKey(to='learn.Author', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='Price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='PublishDate',
            field=models.DateField(),
        ),
    ]
