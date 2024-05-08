from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Example: Directs to a view named 'home'
    # Define other URL patterns for your frontend app here
]
