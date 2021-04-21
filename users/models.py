from django.db import models
from django.contrib.auth.models import User
from sanpham.models import Products
import datetime
from dathang.models import Voucher

# Create your models here.
class User_profile(models.Model):
    owner =models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=True)
    diachi=models.CharField(max_length=100,null=True)
    sdt=models.IntegerField()
    def __str__(self):
        return self.owner.username
    class meta:
         db_table = 'profile-info'
class User_Comment_Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    comment=models.CharField(max_length=300)
    ngaycmt=models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.product.tensp +'/'+self.user.username+ '/' +str(self.ngaycmt)
    
    class meta:
        db_table='User_Comment_Product'
class Voucher_User(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    soluong= models.IntegerField()
    hangsudung=models.DateField()
    sanpham=models.ForeignKey(Products,on_delete=models.CASCADE)