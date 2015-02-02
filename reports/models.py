import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Report(models.Model):

    report_title = models.CharField(max_length=200)
    report_content = models.TextField()
    report_updated = models.DateTimeField(auto_now_add=True)
    report_created = models.DateTimeField(default=datetime.datetime.now, editable=False)
    report_is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.report_title


class Question(models.Model):

    creator = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    date_created = models.DateTimeField(default=datetime.datetime.now)
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



ANSWER_CHOICES = (
    (1, "Very Poor"),
    (2, "Poor"),
    (3, "Fair"),
    (4, "Good"),
    (5, "Excellent"),
    )

class Answer(models.Model):
    answer = models.IntegerField(choices=ANSWER_CHOICES)
    question = models.ForeignKey(Question)
    applicant = models.ForeignKey(User)
    trainer = models.ForeignKey(User)
    date_created = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title


class Rating(models.Model):
    rating = models.ForeignKey(Answer)
    question = models.ForeignKey(Question)
    rated_by = models.ForeignKey(User)
    applicant = models.ForeignKey(User)
    created_on = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.applicant


