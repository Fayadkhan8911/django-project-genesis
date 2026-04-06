from django.shortcuts import render,get_object_or_404
from .models import item as Item # import the item model to use it in the detail view
from django.shortcuts import render, redirect,get_object_or_404
# from django.http import HttpResponse
# from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import itemform
from .models import item

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

@login_required ## this is to require the user to be logged in to access the create view, if the user is not logged in, it will redirect them to the login page defined in the LOGIN_URL setting
def new(request):
    if request.method == 'POST': ## this is to check if the form is submitted, if the request method is POST, it means the form is submitted and we need to process the form data
        form = itemform(request.POST, request.FILES) ## this is to create an instance of the NewItemForm with the submitted data and files, we need to pass request.FILES to handle file uploads (like images)
        if form.is_valid(): ## this is to check if the form data is valid according to the validation rules defined in the form class
            item = form.save(commit=False) ## this is to save the form data to create a new item object, but we set commit=False to prevent it from saving to the database yet, we need to set the owner of the item before saving
            item.created_by = request.user ## this is to set the owner of the new item to the currently logged-in user, we can access the logged-in user through request.user
            item.save() ## this is to save the new item object to the database after setting the owner
            return redirect('item:detail', pk=item.pk) ## this is to redirect the user to the item detail page after successfully creating a new item, you can change it to any page you want
    else:

        form=itemform() ## this is to create an instance of the NewItemForm to pass it to the template, the form will be used to display the form fields in the template and     handle the form submission
    return render(request,'item/form.html', {'form': form,'title': 'New Item'}) ## this is to render the form.html template and pass the form and title to