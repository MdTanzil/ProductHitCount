from django.shortcuts import render
import requests
from . models import Product,ProductViewCounter
import json
# Create your views here.
def home(request):
    template_name = 'home.html'
    context = {}



    # url = 'https://jsonplaceholder.typicode.com/posts'
    # r = requests.get(url)
    # droplets = r.json()

    # for item in droplets:
    #     product = Product.objects.create(
    #        userId = item['userId'],
    #        title = item['title'],
    #        body = item['body'],

    #     )
        # product.save()

    return render(request,template_name,context)

def data(request):
    template_name = 'home.html'
    context = {}
    if request.body:
        data =json.loads(request.body)
        for d in data:
            print(d)
            # model = ProductViewCounter.objects.get(id  = 1)
            # print(d['product_id'])
            print(model)
    return render(request,template_name,context)


