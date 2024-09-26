from django.shortcuts import render
from .models import post

# Create your views here.
def index(request):
    #fetch all posts from db and show in app1_index
    posts = post.objects.all
    return render(request, "app1_index.html", {"posts" : posts})