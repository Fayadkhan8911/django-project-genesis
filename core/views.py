from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from item.models import category,item
from .forms import signupform  

def index(request):
    items = item.objects.filter(is_sold=False).order_by('-created_at')[:6] ## this is to get the latest 10 items that are not sold and order them by created_at in descending orderc
    categories = category.objects.all() ## this is to get all the categories
    return render(request,'core/index.html', {
        'items': items, 
        'categories': categories}) ## this is to render the index.html template and pass the items and categories to the template

def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    form= signupform()
    return render(request,'core/signup.html', 
                  {'form': form})

# Create your views here.

# def core(request):
#     template = loader.get_template('inception.html')
    
#     return HttpResponse(template.render()) /media/di-moriarty/Bankai/Work/django_projects/project_genesis/core/templates/Core/index.html


 