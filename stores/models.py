from django.db import models

# Create your models here.
class FoodStore(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.TextField()
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
