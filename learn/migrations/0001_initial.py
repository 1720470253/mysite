# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AuthorID', models.IntegerField(max_length=10)),
                ('Name', models.CharField(max_length=30)),
                ('Country', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=30)),
                ('AuthorID', models.IntegerField(max_length=10)),
                ('Publisher', models.CharField(max_length=30)),
                ('PublishDate', models.IntegerField()),
                ('ISBN', models.IntegerField()),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
