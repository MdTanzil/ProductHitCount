from django.shortcuts import render
import requests
from . models import Product

# Create your views here.
def home(request):
    template_name = 'home.html'
    context = {}



    url = 'https://jsonplaceholder.typicode.com/posts'
    r = requests.get(url)
    droplets = r.json()

    for item in droplets:
        product = Product.objects.create(
           userId = item['userId'],
           title = item['title'],
           body = item['body'],

        )
        product.save()

    return render(request,template_name,context)

def data(request):
    template_name = 'home.html'
    context = {}
   
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    r = requests.get(url)
    droplets = r.json()

    print(droplets['id'])
    
    
        
    return render(request,template_name,context)


