import requests 
import json
from django.shortcuts import render 
from .models import State

def home(request):

    # AUTO-CREATE default row if not present
    state_obj, created = State.objects.get_or_create(
        id=1,
        defaults={"name": "empty"}
    )

    state = state_obj.name

    if state == "empty":
        emptyCount = 1
        occupiedCount = 0
    else:
        emptyCount = 0
        occupiedCount = 1

    return render(request, "index.html", {
        "currentstate": state,
        "emptyCount": emptyCount,
        "occupiedCount": occupiedCount,
    })
