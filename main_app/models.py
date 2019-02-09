from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Treasure(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    # image = models.ImageField(upload_to='treasure_images', default='media/default.png')


    def __str__(self):
        return ("User ID: {0}, Owner: {1}, Name: {2}, Value: {3}, Material: {4}, Location: {5}, Likes: {6}\n".format(self.id, self.user, self.name, self.value, self.material, self.location, self.likes))

