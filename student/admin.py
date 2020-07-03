from django.contrib import admin
from .models import std

class StudentList(admin.ModelAdmin):
    list_display = ['roll','name','std_class']

admin.site.register(std,StudentList)
