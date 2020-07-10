from django.urls import path
from .views import post_list,post_details,category_list,category_detail
urlpatterns=[
    path('list',post_list,name='post-list'),
    path('details/<int:post_id>',post_details,name='post-details'),
    path('category',category_list,name='category-list'),
    path('catdetail/<cat_name>',category_detail,name='cat-detail')
]