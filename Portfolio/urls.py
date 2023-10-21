from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name="ind"),
    path('projects', views.projects, name="projects")
]
