import json

from django.core.cache.backends.locmem import _caches as cache
from django.http import HttpResponse
from django.shortcuts import render

# get rooms from cache
def rooms_reader():
    rooms = []
    for key in cache['us']:
        rooms.append(key)
    print(rooms)
    return rooms


# home page
def index(request):
    rooms = rooms_reader()
    return render(request, "chat_app/index.html", context={'rooms': rooms})


# get the room_name from the url
def room(request, room_name):
    return render(request, "chat_app/room.html", {"room_name": room_name})


# refreshes rooms from cache for index.html
def rooms_return(request):
    rooms = rooms_reader()
    jsn = json.dumps(rooms)
    return HttpResponse(jsn)
