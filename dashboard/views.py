from django.shortcuts import render
from item.models import item 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):
    items = item.objects.filter(created_by=request.user) ## this is to get the items created by the logged in user
    return render(request, 'dashboard/dashboard.html', 
                  {'items': items}) ## this is to render the dashboard.html template and pass the items to the template