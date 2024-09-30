from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post/<int:post_id>/', views.post_detail, name = "post_detail"),
    path('chai_stores/', views.chai_store_view),
]
