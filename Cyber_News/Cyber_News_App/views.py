from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return HttpResponse(
        "I hope this will work"
        article = Article.objects
    )
