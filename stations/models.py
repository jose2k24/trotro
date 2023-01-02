from django.db import models
from profiles.models import UserProfile

# Create your models here.
class StationPoint(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False,help_text='eg: Kaneshie Station 1')
    phone = models.CharField(max_length=120, blank=False)
    slug = models.SlugField(blank=True)
    image_1=models.ImageField(upload_to='station/images/', blank=True, null=True)
    location = models.CharField(max_length=120, blank=True)
    
    def __str__(self):
        return self.name

    # def __str__(self):
    #     return self.user.firstname


    class Meta:
        verbose_name = 'Station Point'
        verbose_name_plural='Station Points'



class Vehicles(models.Model):
    car_number = models.CharField(max_length=120,blank=False)
    driver = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    station = models.ForeignKey(StationPoint, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.car_number

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural='Vehicles'



class Bookman(models.Model):
    bookman= models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True)
    station = models.ForeignKey(StationPoint, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.bookman.user.username

    class Meta:
        verbose_name = 'Bookman'
        verbose_name_plural='Bookmen'
    

class Fare(models.Model):
    origin = models.CharField(max_length=120, blank=True, null=True)
    destination = models.CharField(max_length=120, blank=True, null=True)
    fare = models.DecimalField(max_digits=9, decimal_places=2,blank=True, null=True)
    station = models.ForeignKey(StationPoint,on_delete=models.CASCADE)

        
    class Meta:
        verbose_name ='Transport Fare'

