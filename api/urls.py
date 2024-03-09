from django.urls import path
from carrental.views import cars


urlpatterns = [
   
    path('cars/',cars,name = "cars"),
]
