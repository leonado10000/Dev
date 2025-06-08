from django.urls import path
from . import views

urlpatterns = [
    path('', views.func, name="else"),
    path('WebResume', views.WebResume, name="webresume"),
    path('games', views.games_home, name="games_home"),
    path('terminal', views.terminal_view, name="terminal"),
]