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
        "heading":s[i]
    })

def WebResume(request):
    return render(request,"WebResume.html")