from django.urls import path
from . import views

urlpatterns = [
    path('', views.func),
    path('WebResume', views.WebResume)
]