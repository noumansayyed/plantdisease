from django.db import models

class Leaf(models.Model):
    shape = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    size = models.IntegerField()  # Assuming size is an integer field

    def __str__(self):
        return f"Leaf - {self.shape} ({self.color}, {self.size})"


class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    uniqueId = models.CharField(max_length=6, unique=True)
    rememberMe = models.BooleanField(default=0)

    def __str__(self):
        return self.email
    

class PlantImage(models.Model):
    image = models.ImageField(upload_to='plant_images/')
    
    

class Disease(models.Model):
    imageName = models.CharField(max_length=100)
    diseaseName = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.diseaseName