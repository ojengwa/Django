from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Applicant(models.Model): 
	user = models.OneToOneField(User)
	first_name = models.CharField()
	last_name = models.CharField()
	phone_number = models.CharField()
	address = models.CharField()
	application_date = models.DateField()
	is_valid = models.BooleanField()
	is_active = models.BooleanField()
	cv = models.URLField()
	cover_letter = models.URLField()