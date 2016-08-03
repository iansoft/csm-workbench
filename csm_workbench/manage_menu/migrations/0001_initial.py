# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('url', models.CharField(max_length=225)),
                ('icon', models.CharField(max_length=45, null=True)),
                ('openable', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('parentID', models.IntegerField(null=True)),
                ('deleted', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 't_menu',
            },
        ),
    ]
