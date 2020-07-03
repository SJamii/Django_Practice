from django.urls import path
from .views import std_list,std_detail

urlpatterns=[
    path('list',std_list,name="std-list"),
    path('detail/<int:std_id>',std_detail,name="std-detail")
]