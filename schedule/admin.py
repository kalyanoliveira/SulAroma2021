from django.contrib import admin
# Import schedule/models.py database-interacting functions
from .models import event

# Register your models here.

# Choosing which fields to display in Django's admin website 
class eventAdmin(admin.ModelAdmin):
    list_display = ("name", "whenStart", "description",)

# Registering models, with created display, to Django's admin website
admin.site.register(event, eventAdmin)