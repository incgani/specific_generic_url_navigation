from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('hyderabad/',hyderabad,name='hyderabad'),
    path('mumbai/',mumbai,name='mumbai'),
]