from django.db import models
from django.contrib.auth.models import User
from medical.models import medical

# Create your models here.

class userInfo(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,default=False)
    name = models.CharField(max_length=50)
    contact = models.BigIntegerField(default=0)
    address = models.TextField(max_length=200,default=False)
    
    def __str__(self):
        return self.user.username
    
class ordersInfo(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,default=False)
    med = models.ForeignKey(to=medical,on_delete=models.CASCADE,default=False)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username
    
    
