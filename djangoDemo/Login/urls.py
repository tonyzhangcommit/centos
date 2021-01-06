from django.urls import path
from Login.views import *

urlpatterns = [
    path('api/createuser/', createUser),
]