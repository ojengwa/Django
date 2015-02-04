import datetime
from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.

class ListingManager(models.Manager):

    def create_listing(self, listing, description, end_date):
        
        if not User.is_admin:
            raise ValueError('You must be admin to do this')

        new_listing = Listing.objects.create({
            'listing': listing,
            'description': description,
            'end_date': end_date,
            })



class Listing(models.Model):
    
    listing = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now, editable=False)
    updated = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(editable=True)

    def __str__(self):
        return self.listing


class Application(models.Model):
    applicant = models.ForeignKey(User)
    listing = models.ForeignKey(Listing)
