from django.shortcuts import render
import os
import json
import random as rn
from django.conf import settings
from Portfolio.views import welcoming_user
from Portfolio.models import Visitor
# Create your views here.

s = [
    "Express Love, Seek Empathy",
    "Everyone\'s Love Stands Empty",
    "Embrace Life\'s Surprising Experiences",
    "End Love, Start Emptiness",
    "Escape Limits, Seek Ecstasy",
    "Escape Lies, Seek Euphoria"
]

@welcoming_user
def func(request):
    i = rn.randint(0,len(s)-1)
    return render(request, "else.html", {
        "heading":s[i],
        "theme": {"text_color": "#ffefd5", "bg_color": "#a76b47", "bg_border": "transparent","border_radius": "5px"}
    })

@welcoming_user
def WebResume(request):
    return render(request,"WebResume.html")

@welcoming_user
def games_home(request):
    return render(request,"games/games_home.html")

@welcoming_user
def terminal_view(request):
    themes = {}
    with open(os.path.join(settings.BASE_DIR,'else','static','themes.json'), 'r') as f:
        themes = json.load(f)
    

    current_theme = request.GET.get('theme', 'neon')
    if current_theme not in themes:
        current_theme = 'neon'

    context = {
        'themes_json': json.dumps(themes),
        'current_theme': current_theme,
        'theme': themes[current_theme],
    }
    return render(request, 'terminal.html', context)

@welcoming_user
def visitors(request):
    return render(request, "visitors.html", {
        "visitors": Visitor.objects.all()
    })