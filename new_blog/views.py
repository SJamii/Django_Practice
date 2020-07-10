from django.shortcuts import render
from .models import Posts,Category

def post_list(request):
    list_of_post = Posts.objects.all()
    context = {
        'post': list_of_post
    }
    return render(request,'new_blog/index.html',context)

def post_details(request,post_id):
    take_post = Posts.objects.get(id=post_id)
    context = {
        'single': take_post
    }
    return render(request,'new_blog/post_details.html',context)

def category_list(request):
    cat = Category.objects.all()
    context ={
        'cat_list': cat
    }
    return render(request,'new_blog/category.html',context)
def category_detail(request,cat_name):
    cat_det = Category.objects.get(name = cat_name)
    cat_post = Posts.objects.filter(category=cat_det)
    context = {
        'cat_po':cat_post
    }
    return render(request,'new_blog/category_detail.html',context)
