from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def will(request):
    return HttpResponse('<h1>will scores 50 in wc semis</h1>')




def ravindra(request):
    return HttpResponse('<h1>wonderful younster of nz</h1>')