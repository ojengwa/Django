# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20150202_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_applicant',
            field=models.ForeignKey(related_name='applicant_report', default=2, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='report_author',
            field=models.ForeignKey(related_name='trainer_report', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
