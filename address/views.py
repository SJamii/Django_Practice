from django.shortcuts import render
from .models import district
def district_list(request):
    dis_list = district.objects.all()
    context = {
        'dlist' : dis_list
    }
    return render(request,'address/district_list.html',context)

def district_detail(request,dis_id):
    single_district = district.objects.get(id=dis_id)
    context={
        'dis_info' : single_district
    }
    return render(request,'address/district_detail.html',context)

def add_home(request):
    return render(request,'address/add_home.html')

def add_about(request):
    return render(request,'address/add_about.html')

def add_contact(request):
    return render(request,'address/add_contact.html')