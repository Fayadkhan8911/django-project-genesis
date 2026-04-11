from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboard, name='dashboard'), ## this is to render the dashboard view when the user goes to the dashboard url
]   