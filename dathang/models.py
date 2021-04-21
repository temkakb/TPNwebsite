from django.db import models
from django.contrib.auth.models import User
import datetime
from sanpham.models import Products
from sanpham.models import Products
# Create your models here.
class Order (models.Model):
    trangthai=(("chuaxacnhan","chưa xác nhận"),("daxacnhan","Đã xác nhận"),("danggiao","đang giao"),("dagiaohang","đã giao hàng"))
    stt = models.AutoField(primary_key=True)
    ngaylapdon=models.DateField(blank=True,null=True)
    tongtien=models.IntegerField(null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    trangthaidonhang=models.CharField(max_length=50,choices=trangthai ,blank=True ,null=True)
    def __str__(self):
        return str(self.stt)

    @property
    def tongtientatca(self): # tong tien order
        orderitem = self.order_product_set.all()
        total = sum([item.tongtien for item in orderitem])
        tongtien=total
        return total  

    @property # decorator của fget, fset kiểu ko cần gọi hàm fdel nữa, viết decorator 
    def tongsanpham(self): # tong san pham chitiet sp
        orderitem = self.order_product_set.all()
        total = sum([item.quantity for item in orderitem])
        return total 
        

        
            
        
        

    class meta:
        db_table = 'Order'
    
class diachigiaohang(models.Model):
    ten = models.CharField(max_length=100)
    ho = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    sdt=models.CharField(max_length=20)
    diachi=models.CharField(max_length=300)
    quan=models.CharField(max_length=200)
    loinhan=models.CharField(max_length=500)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        self.order.ngaylapdon=datetime.datetime.now()
        self.order.save()
        super(diachigiaohang, self).save()
    class meta:
        db_table = 'Address'

   
class Order_Product(models.Model):
    quantity=models.IntegerField(null=True,blank=True,default=0)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    Product=models.ForeignKey(Products,on_delete=models.CASCADE)
    Size = models.CharField(null=True,blank=True,max_length=10)
   
    @property
    def tongtien(self):
        total = self.Product.giatien * self.quantity
        return total
    def quantity_change(self,quantity): # không được mua  0 sản phẩm or vượt quá số lượng tồn, trang giỏ hàng- update sp
        self.quantity=quantity
        if self.quantity<=0:
            self.quantity=0
        if self.quantity>=self.Product.soluongtonkho:
            self.quantity=self.Product.soluongtonkho
    

    class meta:
        db_table = 'Order_Product'
   

class Voucher(models.Model):
    mavoucher=models.CharField(max_length=50,primary_key=True)
    phantramgiamgia=models.IntegerField()
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    def __str__(self):
        return self.mavoucher
    class meta:
        db_table='Voucher'
