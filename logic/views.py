from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Greeting
import spotipy

import json

PREFIX = "/play?"
USER = "user="
ID="id="
SECRET="secret="

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse('Hello from Python!')

def f(request):
    '''
    1. extract username, client id and secret
    2. get devices for device id
    3. done'''
    #user, id, secret = getData(reqeust.get_full_path())
    print("received")
    user = "Iz Ho"
    '''id = "e28a9982e181499dbdb8b8ae80e1e993"
    secret = "3cb162e2569e423aa3b1dde6493c9e14"
    scopes = "user-read-playback-state user-modify-playback-state"
    token = spotipy.util.prompt_for_user_token(user, scopes, client_id=id, client_secret=secret, redirect_uri="http://localhost:8888")'''
    token = "BQAHh2r6szVXwPEVCHSrX9C00qBYlEoBJUTMXMZX96cWvLcseDRTcxjRwIDlCdZvvATb0i58s1EAsKxODDgunh32Pk1OS2NdVYNOP9BrLZj7AzSllPzI2e0GEA4CVLc_RYe55gyMg7LZeMpewjL_MHX8eB60"
    sp = spotipy.Spotify(auth=token)
    deviceId = sp.devices()['devices'][0]['id']
    sp.start_playback(device_id=deviceId)
    print("sending response...")
    return HttpResponse(status=200)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
