from django.shortcuts import render
from .models import std

def std_list(request):
    total_std = std.objects.all()
    context = {
        'list_of_std' : total_std
    }
    return render(request,'student/std_list.html',context)

def std_detail(request,std_id):
    student_id = std.objects.get(id=std_id)
    context = {
        'take_info':student_id
    }
    return render(request,'student/std_detail.html',context)
