from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class flavor(models.Model):
    name = models.CharField(max_length=64,unique=True)
    category = models.CharField(max_length=64)
    cost = models.FloatField()
    units = models.IntegerField()

    def __str__(self):
        return f"{self.name.upper()}"
    
    def save(self,*args,**kwargs):
        is_new = self.pk is None
        super().save(*args,**kwargs)
        if is_new:
            instock.objects.create(flavor=self)
  
class instock(models.Model):
    flavor = models.ForeignKey(flavor,on_delete=models.CASCADE,related_name="stock",null=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.flavor}"
    
    def receive(self,amount):
        self.stock += amount
        self.save()
    
