from django.urls import path

from .views import *

app_name='HEMANTH'

urlpatterns=[

    path('virat/',virat,name='virat.html'),
    path('abd/',abd,name='abd'),
]
