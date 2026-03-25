from django.db import models

# Create your models here.
#DB models for the item app
class members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.name
