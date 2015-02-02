# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.IntegerField(choices=[(1, b'Very Poor'), (2, b'Poor'), (3, b'Fair'), (4, b'Good'), (5, b'Excellent')])),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
                ('applicant', models.ForeignKey(related_name='applicant_ratings', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(to='reports.Question')),
                ('rated_by', models.ForeignKey(related_name='trainer_ratings', to=settings.AUTH_USER_MODEL)),
                ('rating', models.ForeignKey(to='reports.Answer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='reports.Question'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='report',
            name='report_created',
        ),
        migrations.AddField(
            model_name='report',
            name='report_applicant',
            field=models.ForeignKey(related_name='applicant_report', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='report_author',
            field=models.ForeignKey(related_name='trainer_report', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='report_created_at',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
            preserve_default=True,
        ),
    ]
