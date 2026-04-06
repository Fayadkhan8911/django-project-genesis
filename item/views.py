from django.shortcuts import render,get_object_or_404
from .models import item as Item # import the item model to use it in the detail view

# Create your views here.
def detail(request, pk):
    # Get the item with the given primary key (pk) or return a 404 error if not found
    # The get_object_or_404 function is a shortcut that tries to retrieve the object and raises a 404 error if it does not exist
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category,is_sold=False).exclude(pk=item.pk)[0:3] ## this is to get the related items that belong to the same category as the item and exclude the item itself, we limit it to 4 items
    # Render the 'item/detail.html' template with the item and related_items context
    # The context is a dictionary where the keys 'item' and 'related_items' will be used in the template to access the item object and the related items queryset
    return render(request, 'item/detail.html', {
        'item': item, 
        'related_items': related_items})

