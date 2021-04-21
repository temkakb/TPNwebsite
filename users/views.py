from django.shortcuts import render,HttpResponse,redirect
from services.form import FormDangKy
from django.contrib import messages
from sanpham.models import Products
from dathang.models import Order_Product
from django.db.models import Max
from django.contrib.auth import authenticate,logout
from django.contrib.auth.models import User
from services.xulyaccount import dangnhap
from dathang.models import *
import re



# Create your views here.
def home(request):
    if request.method=="GET":
        listsp=Products.objects.all()[:10]
        listsp_late=Products.objects.all().order_by('-ngaythemvao')[:5]
        listsp_trending = Products.objects.annotate(soluong_mua=Max('order_product'))[:5] # cai nay se them 1 truong nua
        if request.user.is_authenticated:
            user = request.user
            order, created = Order.objects.get_or_create(user = user,trangthaidonhang="chuaxacnhan")
            items = order.order_product_set.all()
            cartItem = order.tongsanpham
        else:
            items = []
            order={'tongtientatca':0,'tongsanpham':0}
            cartItem = order['tongsanpham']
        # item.num_soluong_mua = so luong sp da dc mua cao nhat
        context= {"listsp":listsp,"listsp_late":listsp_late,"listsp_trending":listsp_trending ,'cartItem':cartItem,"order":order}
        return render(request,'index.html',context)
    if request.method =="POST":
        if request.POST.get("butt_dangnhap"):
            username=request.POST.get('username')
            password=request.POST.get('password')
            return dangnhap(username,password,request,'home') 
def minigame (request):
    if request.method=="GET":
        if request.user.is_authenticated:
            user = request.user
            order, created = Order.objects.get_or_create(user = user,trangthaidonhang="chuaxacnhan")
            items = order.order_product_set.all()
            cartItem = order.tongsanpham
        else:
            items = []
            order={'tongtientatca':0,'tongsanpham':0}
            cartItem = order['tongsanpham']
        context= {'cartItem':cartItem,"order":order}
        return render (request,'minigame.html',context)
    if request.method =="POST":
        if request.POST.get("butt_dangnhap"):
            username=request.POST.get('username')
            password=request.POST.get('password')
            return dangnhap(username,password,request,redir="minigame")        
            
def dangky(request):
    form=FormDangKy() #
    if request.method=="GET":
        if request.user.is_authenticated:
            messages.error(request,"bạn đã đăng nhập")
            return redirect('home')
        else:
            return render(request,'register.html')
    if request.method=="POST": # dang nhap
        if request.POST.get("butt_dangnhap"):
            username=request.POST.get('username')
            password=request.POST.get('password')
            return dangnhap(username,password,request,'home')
        else: # dang ky
            form=FormDangKy(request.POST)
            password1=request.POST.get('password1')
            password2=request.POST.get('password2') # lay password
            email = request.POST.get('email')
            if len(password1)<=8:
                messages.error(request,"Mật khẩu phải trên 8 ký tự") # kiem tra mat khau tren 8 ky tu
                return redirect('register')
            if(password1 != password2):
                messages.error(request,"Mật khẩu không trùng khớp") # kiem tra mat khau co trung nhau hay khong
                return redirect('register')
            match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
            if( not match):
                messages.success(request,"email sai định dạng")
                return redirect('register')            
            if form.is_valid():
                form.save()
                messages.success(request,"tạo mới account thành công, mời bạn đăng nhập")
                return redirect('home')
            else:
                messages.error(request,"Lỗi đăng ký")
                return redirect('register')
            
            
def dangxuat(request):
        logout(request)
        return redirect('home')
def lienhe(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            user = request.user
            order, created = Order.objects.get_or_create(user = user,trangthaidonhang="chuaxacnhan")
            items = order.order_product_set.all()
            cartItem = order.tongsanpham
        else:
            items = []
            order={'tongtientatca':0,'tongsanpham':0}
            cartItem = order['tongsanpham']
        context= {'cartItem':cartItem,"order":order}
        return render(request,'contact.html',context)
    if request.method =="POST":
        if request.POST.get("butt_dangnhap"):
            username=request.POST.get('username')
            password=request.POST.get('password')
            return dangnhap(username,password,request,redir="lienhe")
      

