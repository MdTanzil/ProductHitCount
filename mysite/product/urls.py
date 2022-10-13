from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name= 'home'),
    path('data/', csrf_exempt(views.data),name= 'data'),
]
