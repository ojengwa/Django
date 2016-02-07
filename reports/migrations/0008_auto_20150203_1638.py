# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20150202_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='question',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='rated_by',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='rating',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='report_applicant',
            new_name='applicant',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='report_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='report_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='report_created_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='report_is_public',
            new_name='is_public',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='report_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='report',
            name='report_updated',
        ),
        migrations.AddField(
            model_name='report',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime.now, auto_now_add=True),
            preserve_default=True,
        ),
    ]
