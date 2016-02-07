import datetime

from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.
class Report(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, related_name="trainer_report")
    applicant = models.ForeignKey(User, related_name="applicant_report")
    updated = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title