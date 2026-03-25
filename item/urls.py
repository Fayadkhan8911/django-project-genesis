from django.urls import path
from . import views

# Define the application namespace for URL reversing
app_name = 'item'

urlpatterns = [
    # Define a URL pattern for the item detail view
    # The pattern includes a dynamic segment <int:pk> which captures an integer and passes it as the 'pk' argument to the view
    path('<int:pk>/', views.detail, name='detail'),
]       
