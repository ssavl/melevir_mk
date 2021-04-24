from django.db import models
from django.contrib.auth.models import AbstractUser



class MyUser(AbstractUser):
    full_name = models.CharField(max_length=100, default='User', null=False, blank=False)
    email = models.CharField(max_length=100, default='None', null=False, blank=False)
    billing_address = models.CharField(max_length=300, default='Moscow', null=False, blank=False)
    
    def __str__(self):
      return full_name
    
    
class Ad(models.Model):
  name = models.CharField(max_length=200, default=None, blank=True, null=True)
  user = models.ForeignKey(MyUser, related_name='ad', on_delete=models.CASCADE)
  
  def __str__(self);
  return name
  
  
class Image(models.Model):
  ad = models.ForeignKey(MyUser, related_name='ad', on_delete=models.CASCADE)
  img = models.ImageField(upload_to='media')
  
  def __str__(self):
    return f"Изображение к обьявлению {ad}"
  
