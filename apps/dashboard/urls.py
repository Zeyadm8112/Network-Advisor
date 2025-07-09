from django.urls import path
from .views import dashboard_view  # make sure this exists in views.py

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
]
