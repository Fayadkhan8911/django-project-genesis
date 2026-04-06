from urllib import request
from django.shortcuts import render,redirect
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
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:core') ## this is to redirect the user to the home page after successful signup, you can change it to any page you want
    else:   
        form = signupform() ## this is to create an instance of the signupform to pass it to the template
    return render(request,'core/signup.html', {
        'form': form}) ## this is to render the signup.html template and pass the form to the template, the form will be used to display the form fields in the template and handle the
    
def login(request):
    return render(request,'core/login.html') ## this is to render the login.html template, we will use the built-in LoginView from django.contrib.auth.views to handle the login functionality, we will pass the loginform as the authentication_form to the LoginView in the urls.py file

def logout(request):
    return render(request,'core/logout.html') ## this is to render the logout.html template, we will use the built-in LogoutView from django.contrib.auth.views to handle the logout functionality, we will pass the logout.html template to the LogoutView in the urls.py file

# Create your views here.

# def core(request):
#     template = loader.get_template('inception.html')
    
#     return HttpResponse(template.render()) /media/di-moriarty/Bankai/Work/django_projects/project_genesis/core/templates/Core/index.html


 