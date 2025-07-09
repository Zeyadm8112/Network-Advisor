from django.urls import path
from .views import home_view  # make sure this exists in views.py

urlpatterns = [
    path('', home_view, name='home'),
]
