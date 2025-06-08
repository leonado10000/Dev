from django.shortcuts import render
import random as rn
# Create your views here.

s = [
    "Express Love, Seek Empathy",
    "Everyone\'s Love Stands Empty",
    "Embrace Life\'s Surprising Experiences",
    "End Love, Start Emptiness",
    "Escape Limits, Seek Ecstasy",
    "Escape Lies, Seek Euphoria"
]

def func(request):
    i = rn.randint(0,len(s)-1)
    return render(request, "else.html", {
        "heading":s[i],
        "theme": {"text_color": "#ffefd5", "bg_color": "#a76b47", "bg_border": "transparent","border_radius": "5px"}
    })

def WebResume(request):
    return render(request,"WebResume.html")

def games_home(request):
    return render(request,"games/games_home.html")

import json
from django.shortcuts import render

def terminal_view(request):
    themes = {
        "neon": {
            "text_color": "#00ffea",
            "bg_color": "#1e1e1e",
            "bg_border": "#00ffea",
            "border_radius": "0",
            "prompt_color": "#00ffc8",
            "caret_color": "#ff00ff",
            "scrollbar_track": "#111",
            "scrollbar_thumb": "#00ffea",
            "placeholder_color": "rgba(0, 255, 234, 0.5)"
        },
        "cozy": {
            "text_color": "#ffefd5",
            "bg_color": "#784c30",
            "bg_border": "transparent",
            "border_radius": "5px",
            "prompt_color": "#ffefd5",
            "caret_color": "#ffefd5",
            "scrollbar_track": "#8f5f37",
            "scrollbar_thumb": "#ffefd5",
            "placeholder_color": "rgba(255, 239, 213, 0.5)"
        },
        "dark": {
            "text_color": "#cfd8dc",
            "bg_color": "#000000",
            "bg_border": "#00202f",
            "border_radius": "4px",
            "prompt_color": "#80deea",
            "caret_color": "#80deea",
            "scrollbar_track": "#37474f",
            "scrollbar_thumb": "#80deea",
            "placeholder_color": "rgba(207, 216, 220, 0.5)"
        },
        "pastel": {
            "text_color": "#5d576b",
            "bg_color": "#e6e2d3",
            "bg_border": "#c5c3c6",
            "border_radius": "10px",
            "prompt_color": "#ffb6b9",
            "caret_color": "#ffb6b9",
            "scrollbar_track": "#dcd6f7",
            "scrollbar_thumb": "#ffb6b9",
            "placeholder_color": "rgba(93, 87, 107, 0.5)"
        },
        "matrix": {
            "text_color": "#00ff00",
            "bg_color": "#000000",
            "bg_border": "#00ff00",
            "border_radius": "0",
            "prompt_color": "#00ff00",
            "caret_color": "#00ff00",
            "scrollbar_track": "#111111",
            "scrollbar_thumb": "#00ff00",
            "placeholder_color": "rgba(0, 255, 0, 0.5)"
        }
    }

    # Get theme name from query param, default to neon
    current_theme = request.GET.get('theme', 'neon')
    if current_theme not in themes:
        current_theme = 'neon'

    context = {
        'themes_json': json.dumps(themes),
        'current_theme': current_theme,
        'theme': themes[current_theme],
    }
    return render(request, 'terminal.html', context)
