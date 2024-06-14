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
    salesman = models.CharField("Salesman", max_length = 100, default = '')
    type = models.CharField('Type', max_length = 30, default = '')
    linkToSize = models.CharField('Link', max_length = 30, default = "")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
# Create your models here.
class SalesMan(models.Model):
    name = models.CharField("Salesman Name", max_length = 30)
    salerName = models.CharField(" Name", max_length = 30, default='')
    countofmany = models.CharField("CountOfMoney", max_length = 200)
    descript = models.TextField("Descript", max_length=300) 
    mail = models.EmailField("Mail", max_length = 40)
    phone = models.CharField("phone", max_length = 11, default = '')
    password = models.CharField("Password", max_length = 15, default= "1111")
    salesman_img = models.ImageField(upload_to='images/', blank=True, null = True, default = 'use.jpeg')
    user_img = models.ImageField(upload_to='images/', blank=True, null = True, default = 'USERS.png')
    grade = models.CharField("greade", max_length = 1)
    indif = models.CharField("Индификатор", max_length= 100, default='')
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Salesman'
        verbose_name_plural = 'Salesmans'


class Snikers(models.Model):
    indif = models.CharField("Индификатор", max_length= 100, default='')
    size36 = models.CharField("count size", max_length = 10)
    size37 = models.CharField("count size", max_length = 10)
    size38 = models.CharField("count size", max_length = 10)
    size39 = models.CharField("count size", max_length = 10)
    size40 = models.CharField("count size", max_length = 10)
    size41 = models.CharField("count size", max_length = 10)
    size42 = models.CharField("count size", max_length = 10)
    size43 = models.CharField("count size", max_length = 10)
    size44 = models.CharField("count size", max_length = 10)
    size45 = models.CharField("count size", max_length = 10)

    class Meta:
        verbose_name = 'SnikersSize'
        verbose_name_plural = 'SnikersSizes'
    
class cloth(models.Model):
    indif = models.CharField("Индификатор", max_length= 100, default='')
    s = models.CharField("count size", max_length = 10)
    m = models.CharField("count size", max_length = 10)
    l = models.CharField("count size", max_length = 10)
    xl = models.CharField("count size", max_length = 10)
    xxl = models.CharField("count size", max_length = 10)
    class Meta:
        verbose_name = 'ClothSize'
        verbose_name_plural = 'ClothSizes'

class CustomUser(AbstractUser):
    phone = models.CharField('phone', max_length = 12 )
    user_img = models.ImageField(upload_to='images/', blank=True, null = True,  default='default.png')
    
    
    groups = models.ManyToManyField(Group, related_name='customuser_groups')  
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions')  

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class CountProduct(models.Model):
    count = models.CharField('Count', max_length= 100)
    indif = models.CharField("Индификатор", max_length= 100, default='')

    class Meta:
        verbose_name = 'Count'
        verbose_name_plural = 'Counts'
    