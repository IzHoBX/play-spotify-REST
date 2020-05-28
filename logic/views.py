from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Greeting

import json

PREFIX = "/agent?sentence="

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse('Hello from Python!')

def f(request):

    print("sending response...")

     return HttpResponse(status=200)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
