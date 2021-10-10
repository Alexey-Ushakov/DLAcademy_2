from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('1', index2, name="index2")
]