from django.urls import path
from instagram.views import *
app_name='something'

urlpatterns=[
    path('reels/',reels,name='reels'),
]