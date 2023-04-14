from django.contrib import admin
# Import home/models.py database-interacting functions
from .models import carouselSlide

# Register your models here.

# Choosing which fields to display in Django's admin website 
class carouselSlideAdmin(admin.ModelAdmin):
    list_display = ('title','slideNumber',)

# Registering models, with created display, to Django's admin website
admin.site.register(carouselSlide, carouselSlideAdmin)