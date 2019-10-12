from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import base64
import .visionAPI
from .models import Greeting

# Create your views here.
@csrf_exempt
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


@csrf_exempt
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


@csrf_exempt
def requests(request):
    if request.method == 'GET':
        return render(request, "index.html")
    elif request.method == 'POST':
        # return HttpResponse("Post request recieved")

        return HttpResponse(request.body)

@csrf_exempt
def images(request):
    if request.method == 'POST':
        url = request.body['image_url']
        return HttpResponse(imageURLToFoodID(url))
    elif request.method == 'GET':
        return render(request, "imageView.html")
