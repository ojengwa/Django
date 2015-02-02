# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=23)),
                ('last_name', models.CharField(max_length=23)),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=40)),
                ('application_date', models.DateField()),
                ('is_valid', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('cv', models.URLField()),
                ('cover_letter', models.URLField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
