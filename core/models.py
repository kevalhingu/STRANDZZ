from django.db import models

# Create your models here.

class contact(models.Model): 
    Contname=models.CharField(max_length=50)
    Contactemail=models.EmailField(max_length=50)
    Contactphone=models.CharField(max_length=50)
    Contactreason=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Contname