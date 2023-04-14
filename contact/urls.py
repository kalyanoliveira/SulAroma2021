from django.urls import path
#Import views.py functions
from . import views

#Define app name
app_name = 'contact'

#Define ULR that gets the user to contact/speaker's page
urlpatterns = [
    path('', views.index, name="index")
]