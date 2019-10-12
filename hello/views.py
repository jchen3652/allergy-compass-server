from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import base64
import json
from google.cloud import vision
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
        data = json.loads(request.data)
        url = data['image_url']


        return HttpResponse(imageURLToFoodID(url))
    elif request.method == 'GET':
        return render(request, "imageView.html")

def imageURLToFoodID(url):
    """Search similar products to image.
    Args:
        url
    """
    # product_search_client is needed only for its helper methods.
    product_search_client = vision.ProductSearchClient()
    image_annotator_client = vision.ImageAnnotatorClient()

    #TODO: this may be incorrect for network stuff
    with open(url, 'rb') as image_file:
        content = image_file.read()

    # Create annotate image request along with product search feature.
    image = vision.types.Image(content=content)

    # product search specific parameters
    product_set_path = product_search_client.product_set_path(
        project=project_id, location=location,
        product_set=product_set_id)
    product_search_params = vision.types.ProductSearchParams(
        product_set=product_set_path,
        product_categories=[product_category],
        filter=filter)
    image_context = vision.types.ImageContext(
        product_search_params=product_search_params)

    # Search products similar to the image.
    response = image_annotator_client.product_search(
        image, image_context=image_context)

    results = response.product_search_results.results

    return results[0].product.name
