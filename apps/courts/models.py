from django.db import models
from apps.users.models import User
from localflavor.us.models import USStateField, USZipCodeField

# Create your models here.

class CourtManager(models.Model):
    def create_court(self, form_data):
        return self.create( 
            name        =   form_data['title'],
            address     =   form_data['address'],
            city        =   form_data['city'],
            state       =   form_data['state'],
            zipcode     =   form_data['zipcode'],
            description =   form_data['desc'],
            price       =   form_data['price']
        )

class Court(models.Model):
    name    = models.CharField(max_length=255)
    address  = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = USStateField()
    zipcode = USZipCodeField()
    description = models.TextField()
    price      = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourtManager()

    def __str__(self):
        return self.name

class SelectedCourt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    timein = models.DateTimeField()
    timeout = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
