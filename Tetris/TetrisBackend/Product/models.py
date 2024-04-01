from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class ProductModel(models.Model):
    name = models.CharField('NameOfProduct', max_length = 25)
    description = models.TextField('Description', max_length = 500)
    price = models.CharField('Price', max_length = 10)
    img1 = models.ImageField(upload_to='images/')
    img2 = models.ImageField(upload_to='images/')
    img3 = models.ImageField(upload_to='images/')
    dateOfPublic = models.DateField("DateOfPublic")
    discount = models.CharField("Скидка", max_length = 10)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField('phone', max_length = 12 )
    user_img = models.ImageField(upload_to='images/', blank=True, null = True,  default='default.png')
    
    
    groups = models.ManyToManyField(Group, related_name='customuser_groups')  
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions')  

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
