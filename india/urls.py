from india.views import *

from django.urls import path
app_name='rohit'

urlpatterns=[
    path('virat/',virat,name='virat'),
    path('shreyas/',shreyas,name='shreyas'),
]