from django.urls import path

from .views import *

app_name='HEMANTH'

urlpatterns=[

    path('rohit/',rohit,name='rohit.html'),
    path('sky/',sky,name='sky'),
]