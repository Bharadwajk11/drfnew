# urls.py in your testapp

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL for the home view
]
