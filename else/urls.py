from django.urls import path
from . import views

urlpatterns = [
    path('', views.func, name="else"),
    path('WebResume', views.WebResume),
]