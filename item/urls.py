from django.urls import path
from . import views

# Define the application namespace for URL reversing
app_name = 'item'

urlpatterns = [
    # Define a URL pattern for the item detail view
    # The pattern includes a dynamic segment <int:pk> which captures an integer and passes it as the 'pk' argument to the view
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'), ## this is to define a URL pattern for the item creation view, it will be accessed at /item/new/
    path('<int:pk>/delete/', views.delete_item, name='delete'), ## this is to define a URL pattern for the item deletion view, it will be accessed at /item/delete/<pk>/

]       
