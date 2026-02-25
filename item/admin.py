from django.contrib import admin
from .models import category,item

# Register your models here.
## this is to register the 'category' model in the admin panel
admin.site.register(category)
admin.site.register(item) 