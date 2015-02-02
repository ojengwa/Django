# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20150202_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_applicant',
            field=models.ForeignKey(related_name='applicant_report', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='report_author',
            field=models.ForeignKey(related_name='trainer_report', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
