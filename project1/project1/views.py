from django.http import HttpResponse

def home(request):
    return HttpResponse("Youre in homepage")

def about(request):
    return HttpResponse("Youre in about section")

def contact(request):
    return HttpResponse("Youre in contact page")