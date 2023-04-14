from django.urls import path
#Import views.py functions
from . import views

#Define app name
app_name = 'schedule'

#Define ULR that gets the user to a schedule/events page
urlpatterns = [
    path('', views.index, name="index")
]