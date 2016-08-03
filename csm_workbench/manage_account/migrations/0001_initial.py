# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 't_role',
            },
        ),
        migrations.CreateModel(
            name='RoleMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu', models.ForeignKey(to='manage_menu.Menu')),
                ('role', models.ForeignKey(to='manage_account.Role')),
            ],
            options={
                'db_table': 't_role_menu',
            },
        ),
    ]
