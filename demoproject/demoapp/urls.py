from . import views
from django.urls import path
urlpatterns =[
    path('',views.demo,name='demo'),
    path('forms/',views.forms,name='about'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('thanks/',views.thanks,name='thanks'),
    path('add/',views.results,name='results')
]