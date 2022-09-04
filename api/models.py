from django.db import models

class  Location(models.Model):
    id = models.AutoField(primary_key=True)
    fsq_id=models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    country = models.TextField()
    region = models.TextField()
    name = models.TextField()

    
