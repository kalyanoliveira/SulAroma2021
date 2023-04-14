from django.db import models
# Import RichTextField. Requires pip install django-ckeditor
from ckeditor.fields import RichTextField
# Import timezone now module for auto adding created_on
from django.utils import timezone

# Create your models here

# Author SQL database table. Columns: name
class blogAuthor(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__ (self):
        return f"{self.name}"

# Blog post SQL database table. Columns: title, publish data, lead-in, body, thumbnail image, author
class blogPost(models.Model):
    title = models.CharField(max_length=64)
    created_on = models.DateTimeField(default=timezone.now)
    lead_in = models.CharField(blank=True, max_length=256)
    # RichTextField implementation
    body = RichTextField(blank=True)
    # upload_to tells Django to store thumbnail images in media/blogThumbnails/
    thumbnail = models.ImageField(upload_to='blogThumbnails/')
    # on_delete tells Django to delete blog post rows from SQL database if corresponding author row is deleted
    author = models.ForeignKey(blogAuthor, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return f"{self.title}"

# Blog post SQL database table. Columns: author, publish date, body, belongs to post
class blogComment(models.Model):
    author = models.CharField(max_length=64)
    created_on = models.DateTimeField(default=timezone.now)
    # No need for length restriction, user is never able to submit more than 1024. Gives more freedom in editing of comments
    body = models.TextField()
    # related_name allows blogPost.objects.get(pk=<int>).comments syntax
    # on_delete tells Django to delete blog comment rows from SQL database if corresponding blog post row is deleted
    post = models.ForeignKey(blogPost, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.author}"