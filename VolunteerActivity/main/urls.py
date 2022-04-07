from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name=''),
    path('project', project, name='project'),
    path('volunteer', volunteer, name='volunteer'),
    path('volunteerhelp', volunteerhelp, name='volunteerhelp'),
    path('contacts', contacts, name='contacts')
]
