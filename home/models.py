from django.db import models

# Create your models here.

# Carousel slide SQL database table. Columns:
class carouselSlide(models.Model):
    # upload_to tells Django to store profile pictures in media/carouselImages/
    image = models.ImageField(upload_to="carouselImages/")
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    slideNumber = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"