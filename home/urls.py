from django.urls import path
#Import views.py functions
from . import views

#Define app name
app_name = 'home'

#Define ULR that gets the user to home page
urlpatterns = [
    path('', views.index, name="index")
]