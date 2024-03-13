from django.db import models

class MiningData(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6)    
    cu_grade = models.DecimalField(max_digits=4, decimal_places=2)