# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('report_title', models.CharField(max_length=200)),
                ('report_content', models.TextField()),
                ('report_updated', models.DateTimeField(auto_now_add=True)),
                ('report_created', models.DateTimeField(default=datetime.datetime.now)),
                ('report_is_public', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
