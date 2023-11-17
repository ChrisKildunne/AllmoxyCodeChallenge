# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('receiver_path/', views.webhook, name='webhook'),
]
