from django.urls import path
from google.views import *
app_name='web'

urlpatterns=[
    path('search/',search,name='search'),
]