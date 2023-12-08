from nz.views import *

from django.urls import path
app_name='philips'

urlpatterns=[
    path('will/',will,name='will'),
    path('ravindra/',ravindra,name='ravindra'),
]