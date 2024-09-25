from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Youre in homepage")
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return HttpResponse("Youre in contact page")