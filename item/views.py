from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Item

# Create your views here.
def detail(request, pk):
    # Get the item with the given primary key (pk) or return a 404 error if not found
    # The get_object_or_404 function is a shortcut that tries to retrieve the object and raises a 404 error if it does not exist
    item = get_object_or_404(Item, pk=pk)
    # Render the 'item/detail.html' template with the item context
    # The context is a dictionary where the key 'item' will be used in the template to access the item object
    return render(request, 'item/detail.html', {'item': item})