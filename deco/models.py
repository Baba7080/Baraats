from django.db import models

class ServiceNeed(models.Model):
    Service= models.CharField(max_length=100)
    Phone_no=models.CharField(max_length=12)
    pin = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    def __str__(self):
        return self.city
    