from django.shortcuts import render
from .models import post, ChaiVariety, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.
def index(request):
    #fetch all posts from db and show in app1_index
    posts = post.objects.all
    return render(request, "app1_index.html", {"posts" : posts})    

def post_detail(request, post_id):
    #fetch post with post_id
    temp = get_object_or_404(post, pk = post_id)
    return render(request, "post_page.html", {"post" : temp})

def chai_store_view(request):
    stores = None
    if(request.method == 'POST'):
        #form submit request
        form = ChaiVarietyForm(request.POST)
        if(form.is_valid()):
            chai_variety = form.cleaned_data["chai_variety"]              #chai_variety is field name in forms.py
            stores = Store.objects.filter(chai_varieties = chai_variety)
    else:
        form = ChaiVarietyForm()                #if simple get request, render form
    
    return render(request, 'chai_stores.html', {'form' : form, "stores" : stores})