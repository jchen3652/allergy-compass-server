from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import base64
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
        img_data = request.body["img"]
        with open("static/image.png", "wb") as fh:
            fh.write(base64.decodebytes(img_data))
        return HttpResponse("All good")
    elif request.method == 'GET':
        return render(request, "imageView.html")