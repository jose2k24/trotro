from django.contrib import admin
from .models import StationPoint, Vehicles,Bookman, Fare

# # Register your models here.
admin.site.register(StationPoint)
admin.site.register(Bookman)
admin.site.register(Vehicles)
admin.site.register(Fare)