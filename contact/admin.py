from django.contrib import admin
# Import contact/models.py database-interacting functions
from .models import speaker

# Register your models here.

# Choosing which fields to display in Django's admin website 
class speakerAdmin(admin.ModelAdmin):
    list_display = ("name",)

# Registering models, with created display, to Django's admin website
admin.site.register(speaker, speakerAdmin)