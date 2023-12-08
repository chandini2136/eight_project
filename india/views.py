from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h1>50 th century in ODI</h>')



def shreyas(request):
    return HttpResponse('<h1>shreyas has scored century in wc semis</h1>')