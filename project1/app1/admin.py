from django.contrib import admin
from .models import post, ChaiVariety, ChaiReview, Store, ChaiCert

# Register your models here.                
admin.site.register(ChaiVariety)               #shows post model in admin panel
admin.site.register(ChaiReview) 
admin.site.register(Store) 
admin.site.register(ChaiCert) 