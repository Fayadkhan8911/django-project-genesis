from django.db import models
from django.contrib.auth.models import User

# Create your models here.
## this is the category model that will be used to create the categories for the items
class category(models.Model):
    name = models.CharField(max_length=255)
## return the name of the category when we call it in the admin panel
    class Meta:
        ordering = ['name'] ## this is to order the categories by name in the admin panel
        verbose_name_plural = "categories"


## this is to return the name of the category when we call it in the admin panel
    def  __str__(self):
        return self.name

class item(models.Model):
    ## this is to store the name of the item
    name = models.CharField(max_length=255)
    ## this is to store the description of the item
    description = models.TextField() 
    ## this is to store the price of the item with 10 digits and 2 decimal places
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    ## this is to upload the image of the item and store it in the 'item_images' folder in the media folder
    image= models.ImageField(upload_to='item_images/',blank=True, null=True)
    ## this is to create a foreign key relationship with the category model and delete the item if the category is deleted
    category = models.ForeignKey(category,related_name="items" ,on_delete=models.CASCADE) 
    ## this is to store the status of the item whether it is sold or not, default is False
    is_sold = models.BooleanField(default=False) 
    ## this is to store the date and time when the item is created, it will be automatically set to the current date and time when the item is created
    created_at = models.DateTimeField(auto_now_add=True) 
    ## this is to create a foreign key relationship with the User model and delete the item if the user is deleted, related_name is used to access the items created by the user in the user model
    created_by = models.ForeignKey('auth.User',related_name='items',on_delete=models.CASCADE) 

    class Meta:
        ordering = ['name'] ## this is to order the items by name in the admin panel
    
    def  __str__(self):
        return self.name