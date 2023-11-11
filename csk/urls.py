from django.urls import path

from csk.views import *

app_name='HEMANTH'

urlpatterns=[

    path('msd/',msd,name='msd.html'),
    path('jadeja/',jadeja,name='jadeja'),
]
