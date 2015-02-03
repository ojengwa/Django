import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Report(models.Model):

    report_title = models.CharField(max_length=200)
    report_content = models.TextField()
    report_author = models.ForeignKey(User, related_name="trainer_report")
    report_applicant = models.ForeignKey(User, related_name="applicant_report")
    report_updated = models.DateTimeField(auto_now_add=True)
    report_created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    report_is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.report_title
