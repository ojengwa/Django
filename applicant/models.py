from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Applicant(models.Model): 
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length = 23)
	last_name = models.CharField(max_length = 23)
	phone_number = models.CharField(max_length = 15)
	address = models.CharField(max_length = 45)
	application_date = models.DateField(auto_now = True)
	is_valid = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)
	cv = models.URLField()
	cover_letter = models.URLField()