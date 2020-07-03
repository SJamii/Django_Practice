from django.urls import path
from .views import district_list,district_detail,add_home,add_about,add_contact
urlpatterns = [
    path('list',district_list,name="district-list"),
    path('detail/<int:dis_id>',district_detail,name="district-detail"),
    path('home',add_home,name='add-home'),
    path('about',add_about,name='add-about'),
    path('contact',add_contact,name="add-contact")
]