from django.urls import path
#Import views.py functions
from . import views

#Define app name
app_name = 'blog'

#Define ULR that gets the user to a blog page
urlpatterns = [
    path('<int:pIntVariable>', views.index, name="index") # <int:pIntVariable> allows for display of desired post during initial display of blog webpage. Made by means of a relationship between the pk SQL column of blog posts (pk value is supplied by ULR) and template context variables. Processing in blog/views.py
]