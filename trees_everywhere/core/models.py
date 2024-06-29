from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    def plant_tree(self, plant, location, account):
        planted_tree = PlantedTree.objects.create(user=self, plant=plant, latitude=location[0], longiture=location[1], account=account)
        return planted_tree

    def plant_trees(self, plantings, account):
        for plant, location in plantings:
            self.plant_tree(plant, location, account)


    def get_profile(self,):
        profile = Profile.objects.filter(user=self)
        if profile.count():
            return profile.first()
        return None       

         

class Account(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='accounts')

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True, default='')
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Plant(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PlantedTree(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longiture = models.DecimalField(max_digits=9, decimal_places=6)
    planted_at = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(default=0)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.plant.name} plantada por {self.user.username}'
    
    def location(self):
        return (self.latitude, self.latitude)

