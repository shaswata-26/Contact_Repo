from django.urls import path 
from .  import views

urlpatterns=[
    path('',views.contact_view,name='contactview'),
    path('get/',views.getData,name='getdata'),

]