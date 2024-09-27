from django.shortcuts import render
from .models import post
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    #fetch all posts from db and show in app1_index
    posts = post.objects.all
    return render(request, "app1_index.html", {"posts" : posts})    

def post_detail(request, post_id):
    #fetch post with post_id
    temp = get_object_or_404(post, pk = post_id)
    return render(request, "post_page.html", {"post" : temp})