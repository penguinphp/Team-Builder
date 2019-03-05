# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-03-04 20:53
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190303_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('android', 'Android Developer'), ('designer', 'Designer'), ('java', 'Java Developer'), ('php', 'PHP Developer'), ('python', 'Python Developer'), ('rails', 'Rails Developer'), ('wordpress', 'Wordpress Devloper'), ('ios', 'iOS Developer')], default='', max_length=52),
            preserve_default=False,
        ),
    ]
