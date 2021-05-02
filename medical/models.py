from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class medical(models.Model):
    user = models.ForeignKey(to=User,default=False,on_delete=models.CASCADE)
    name_of_med = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    contact = models.BigIntegerField()
    reg_num = models.IntegerField()
    est = models.IntegerField()
    
    def __str__(self):
        return self.user.username
    
class MedStocks(models.Model):
    user = models.ForeignKey(to=User,default=False,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.BigIntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username}:{self.name}"
    
    
    


