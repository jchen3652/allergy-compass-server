from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import base64
import json
import requests
from google.cloud import vision
from .models import Greeting

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'allergy-compass',
})

dataBase = firestore.client()

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
def preferenceUpdate(request):
    print("Request body: ", request.body)
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name'] 
        dairy = (data['Dairy'] in ["true","True"])
        soy = (data['Soy'] in ["true","True"])
        seafood = (data['Seafood'] in ["true","True"])
        nuts = (data['Nuts'] in ["true", "True"])
        doc_ref = dataBase.collection('users').document(name)
        doc_ref.set({
            'name':name,
            'Dairy':dairy,
            'Soy':soy,
            'Seafood':seafood,
            'Nuts':nuts

        })
    return JsonResponse(data)
@csrf_exempt
def login(request):
    print("Request body: ", request.body)
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        password = data['password']
        response = {}
        doc_ref = dataBase.collection('users').document(name)
        try:
            doc = doc_ref.get()
            if (doc.to_dict()['password']==password):
                print("good")
                response["good"] = "good"
            else:
                response["good"] = "bad"
        except google.cloud.exceptions.NotFound:
            response["good"] = "no doc"
    print(response)
    return JsonResponse(response)


@csrf_exempt
def getPrefs(request):
    print("Request body: ", request.body)
    if request.method == 'GET':
        data = json.loads(request.body)
        name = data['name']
        response = {}
        doc_ref = dataBase.collection('users').document(name)
        try:
            doc = doc_ref.get()
            dic = doc.to_dict()
            response["soy"] = dic["Soy"]
            response["seafoood"] = dic["Seafood"]
            response["nuts"] = dic["Nuts"]
            response["dairy"] = dic["Dairy"]
            

        except google.cloud.exceptions.NotFound:
            response[""] = "no doc"
    print(response)
    return JsonResponse(response)

@csrf_exempt
def getSoy(request):
    print("Request body: ", request.body)
    if request.method == 'GET':
        data = json.loads(request.body)
        name = data['name']
        response = {}
        doc_ref = dataBase.collection('users').document(name)
        try:
            doc = doc_ref.get()
            dic = doc.to_dict()
            response["soy"] = dic["Soy"]
        except google.cloud.exceptions.NotFound:
            response["soy"] = False
    print(response)
    return JsonResponse(response)

@csrf_exempt
def getSeafood(request):
    print("Request body: ", request.body)
    if request.method == 'GET':
        data = json.loads(request.body)
        name = data['name']
        response = {}
        doc_ref = dataBase.collection('users').document(name)
        try:
            doc = doc_ref.get()
            dic = doc.to_dict()
            response["seafood"] = dic["Seafood"]
        except google.cloud.exceptions.NotFound:
            response["seafood"] = False
    print(response)
    return JsonResponse(response)

@csrf_exempt
def getNuts(request):
    print("Request body: ", request.body)
    if request.method == 'GET':
        data = json.loads(request.body)
        name = data['name']
        response = {}
        doc_ref = dataBase.collection('users').document(name)
        try:
            doc = doc_ref.get()
            dic = doc.to_dict()
            response["nuts"] = dic["Nuts"]
        except google.cloud.exceptions.NotFound:
            response["nuts"] = False
    print(response)
    return JsonResponse(response)

@csrf_exempt
def getDairy(request):
    print("Request body: ", request.body)
    if request.method == 'GET':
        data = json.loads(request.body)
        name = data['name']
        response = {}
        doc_ref = dataBase.collection('users').document(name)
        try:
            doc = doc_ref.get()
            dic = doc.to_dict()
            response["dairy"] = dic["Dairy"]
        except google.cloud.exceptions.NotFound:
            response["dairy"] = False
    print(response)
    return JsonResponse(response)

@csrf_exempt
def addUser(request):
    print("Request body: ", request.body)
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        password = data['password']
        doc_ref = dataBase.collection('users').document(name)
        doc_ref.set({
            'name': name,
            'password': password,
        })
    return JsonResponse(data)


@csrf_exempt
def images(request):
    print("Request body:",request.body)

    if request.method == 'POST':
        data = json.loads(request.body)
        url = data['image_url']


        # return HttpResponse(imageURLToFoodID(url))

        data = {
        'food': imageURLToFoodID(url)
        }

        return JsonResponse(data)



    elif request.method == 'GET':
        return render(request, "imageView.html")

#
#
# def get_similar_products_file(
#         project_id, location, product_set_id, product_category,
#         file_path, filter):
#     """Search similar products to image.
#     Args:
#         project_id: Id of the project.
#         location: A compute region name.
#         product_set_id: Id of the product set.
#         product_category: Category of the product.
#         file_path: Local file path of the image to be searched.
#         filter: Condition to be applied on the labels.
#         Example for filter: (color = red OR color = blue) AND style = kids
#         It will search on all products with the following labels:
#         color:red AND style:kids
#         color:blue AND style:kids
#     """
#     # product_search_client is needed only for its helper methods.
#     product_search_client = vision.ProductSearchClient()
#     image_annotator_client = vision.ImageAnnotatorClient()
#
#     # Read the image as a stream of bytes.
#     with open(file_path, 'rb') as image_file:
#         content = image_file.read()
#
#     # Create annotate image request along with product search feature.
#     image = vision.types.Image(content=content)
#
#     # product search specific parameters
#     product_set_path = product_search_client.product_set_path(
#         project=project_id, location=location,
#         product_set=product_set_id)
#     product_search_params = vision.types.ProductSearchParams(
#         product_set=product_set_path,
#         product_categories=[product_category],
#         filter=filter)
#     image_context = vision.types.ImageContext(
#         product_search_params=product_search_params)
#
#     # Search products similar to the image.
#     response = image_annotator_client.product_search(
#         image, image_context=image_context)
#
#     # print(response)
#
#     index_time = response.product_search_results.index_time
#     print('Product set index time:')
#     print('  seconds: {}'.format(index_time.seconds))
#     print('  nanos: {}\n'.format(index_time.nanos))
#
#     results = response.product_search_results.
#
#     return results[0].product.name
#


def get_similar_products_uri(
        project_id, location, product_set_id, product_category,
        image_uri, filter):
    """Search similar products to image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
        product_category: Category of the product.
        file_path: Local file path of the image to be searched.
        filter: Condition to be applied on the labels.
        Example for filter: (color = red OR color = blue) AND style = kids
        It will search on all products with the following labels:
        color:red AND style:kids
        color:blue AND style:kids
    """
    # product_search_client is needed only for its helper methods.
    product_search_client = vision.ProductSearchClient()
    image_annotator_client = vision.ImageAnnotatorClient()

    # Create annotate image request along with product search feature.
    image_source = vision.types.ImageSource(image_uri=image_uri)
    image = vision.types.Image(source=image_source)

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

    print(response)

    results = response.product_search_results.results

    return results[0].product.name




def imageURLToFoodID(url):
    project_id = 'allergy-compass'

    location = 'us-east1'
    product_set_id = 'product_set0'
    product_category = 'packagedgoods-v1'
    filter = 'style=nothing'


    """Search similar products to image.
    Args:
        url
    """


    import requests
    f = open('temp.jpg','wb')
    f.write(requests.get(url).content)
    f.close()



    # product_search_client is needed only for its helper methods.
    product_search_client = vision.ProductSearchClient()
    image_annotator_client = vision.ImageAnnotatorClient()

    #TODO: this may be incorrect for network stuff
    with open('temp.jpg', 'rb') as image_file:
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

    print(response)

    results = response.product_search_results.results

    return results[0].product.name
