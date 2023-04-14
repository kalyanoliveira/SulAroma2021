from django.db import models

# Create your models here.

# Speaker SQL database table. Columns: profile picture, name, biography
class speaker(models.Model):
    # upload_to tells Django to store profile pictures in media/profilePictures/
    profilePicture = models.ImageField(upload_to="profilePictures/")
    name = models.CharField(max_length=64)
    biography = models.TextField()

    def __str__(self):
        return f"{self.name}"