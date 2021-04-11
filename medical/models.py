from django.db import models

# Create your models here.

class medical(models.Model):
    name_of_med = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    contact = models.BigIntegerField()
    reg_num = models.IntegerField()
    est = models.IntegerField()
    
    def __str__(self):
        return self.name_of_med
    
    


