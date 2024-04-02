from django.urls import path
from facebook.views import *
app_name='image'

urlpatterns=[
    path('page/',page,name='page')

]