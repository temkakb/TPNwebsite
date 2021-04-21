from django.db import models
import datetime
from django.db.models.signals import pre_save
from django.utils.text import slugify

from cloudinary.models import CloudinaryField
# Create your models here.
class Thuonghieu( models.Model):
    mathuonghieu= models.CharField(max_length=300,primary_key=True)
    tenthuonghieu =models.CharField(max_length=300,null=False)
    def __str__(self):
        return self.tenthuonghieu
    class meta:
        db_table = 'Thuonghieu'


class Products(models.Model):
    TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)
    
    loai=(('top',' Áo'),('bottom','Quần'),("coat","Áo khoác"))
    masp = models.CharField(max_length=50,primary_key=True)
    tensp=models.CharField(max_length=200,null=False)
    slug= models.SlugField(max_length=200,null=True,blank=True)
    giatien=models.IntegerField()
    mota=models.CharField(max_length=1000,null=True)
    sizeS=models.BooleanField(choices=TRUE_FALSE_CHOICES,null=True)
    sizeM=models.BooleanField(choices=TRUE_FALSE_CHOICES,null=True)
    sizeL=models.BooleanField(choices=TRUE_FALSE_CHOICES,null=True)
    sizeXL=models.BooleanField(choices=TRUE_FALSE_CHOICES,null=True)
    Loai=models.CharField(max_length=20,choices=loai,default="Unknown")
    rate=models.FloatField(null=True)
    tongrate = models.IntegerField(null=True,blank=True,default=0)
    soluongtonkho=models.IntegerField()
    img=CloudinaryField('image',null=True)
    ngaythemvao=models.DateField(default=datetime.date.today)
    thuonghieu=models.ForeignKey(Thuonghieu,on_delete=models.CASCADE)
    def photo_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url
    def __str__(self):
        return self.tensp
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.tensp)
        
        super(Products, self).save()
    def luurate (self,rate_predict):
        if(self.tongrate is None):
            self.tongrate =int( rate_predict)
            
        else:
            self.tongrate =self.tongrate+ int(rate_predict)
    def tinhrate(self,count):
       self.rate="{:.2f}".format(self.tongrate/count)
            
            

    class meta:
        db_table = 'Products'


