from django.contrib import admin
# Import blog/models.py database-interacting functions
from .models import blogPost, blogComment, blogAuthor

# Register your models here.

# Choosing which fields to display in Django's admin website 
class blogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_on", "lead_in",)

class blogCommentAdmin(admin.ModelAdmin):
    list_display = ("author", "created_on", "post",)

class blogAuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)

# Registering models, with created display, to Django's admin website
admin.site.register(blogPost, blogPostAdmin)
admin.site.register(blogComment, blogCommentAdmin)
admin.site.register(blogAuthor, blogAuthorAdmin)