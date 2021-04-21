from django.shortcuts import render
from .models import Products,Thuonghieu
from users.models import User_Comment_Product
from services.demtrang import demtrang,numtrang
from django.contrib.postgres.search import SearchVector
from AI_WEB.model_AI import dudoan_Rate
from dathang.models import Order
from services.xulyaccount import dangnhap

import datetime
# Create your views here.
def sanpham_page(request):
    if request.method=="GET":
        listsp=Products.objects.all()[:12]
        count=Products.objects.all().count()
        trang=demtrang(count)
        listthuonghieu=Thuonghieu.objects.all()
        if request.user.is_authenticated:
            user = request.user
            order, created = Order.objects.get_or_create(user = user,trangthaidonhang="chuaxacnhan")
            items = order.order_product_set.all()
            cartItem = order.tongsanpham
        else:
            items = []
            order={'tongtientatca':0,'tongsanpham':0}
            cartItem = order['tongsanpham']
        context= {'cartItem':cartItem,"order":order,'items':items,"listsp":listsp,"trang":trang,"listthuonghieu":listthuonghieu}
        return render(request,'product.html',context)
    if request.method=="POST": # dang nhap 
        if request.POST.get("butt_dangnhap"):
            username=request.POST.get('username')
            password=request.POST.get('password')
            return dangnhap(username,password,request,'sanpham_page')
        
def num_sanpham(request,numpage):
    if request.method=="GET":
        count=Products.objects.all().count()
        trang=demtrang(count)
        arr_num_trang= numtrang(numpage)
        start=arr_num_trang[0]
        end=arr_num_trang[1]
        listsp=Products.objects.all()[start:end]
        listthuonghieu=Thuonghieu.objects.all()
        if request.user.is_authenticated:
            user = request.user
            order, created = Order.objects.get_or_create(user = user,trangthaidonhang="chuaxacnhan")
            items = order.order_product_set.all()
            cartItem = order.tongsanpham
        else:
            items = []
            order={'tongtientatca':0,'tongsanpham':0}
            cartItem = order['tongsanpham']
        context= {'cartItem':cartItem,"order":order,'items':items,"listsp":listsp,"trang":trang}
        return render(request,'product.html',context)
def chitietsp (request,id):
    try:
        sp=Products.objects.get(slug=id)
    except:
        return render(request,'404.html')
            # lay cmt nguoi dung
    cmts = User_Comment_Product.objects.all().filter(product=sp)
    demsocmt = User_Comment_Product.objects.all().filter(product=sp).count()
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user = user,trangthaidonhang="chuaxacnhan")
        items = order.order_product_set.all()
        cartItem = order.tongsanpham
    else:
        items = []
        order={'tongtientatca':0,'tongsanpham':0}
        cartItem = order['tongsanpham']
        
    if request.method=="POST": # binh luan
        newcmt = User_Comment_Product.objects.create(user=request.user,product=sp,comment=request.POST.get("comment"),ngaycmt=datetime.datetime.now())
        demsocmt = User_Comment_Product.objects.all().filter(product=sp).count()
        d1=dudoan_Rate(request.POST.get("comment"))
        rate=d1.return_rate()
        sp.luurate(rate)
        sp.tinhrate(demsocmt) 
        newcmt.save()
        sp.save()
    context= {'cartItem':cartItem,"order":order,"sp":sp,"cmts":cmts,"demsocmt":demsocmt}   
    return render(request,'product-detail.html',context)
       
def ao_page(request):
    if request.method=="GET":
        listsp=Products.objects.all().filter(Loai="top")
        count= Products.objects.all().filter(Loai="top").count()
        trang=demtrang(count)
        if request.user.is_authenticated:
            user = request.user
            order, created = Order.objects.get_or_create(user = user,trangthaidonhang="chuaxacnhan")
            items = order.order_product_set.all()
            cartItem = order.tongsanpham
        else:
            items = []
            order={'tongtientatca':0,'tongsanpham':0}
            cartItem = order['tongsanpham']
        context= {'cartItem':cartItem,"order":order,'items':items,"listsp":listsp,"trang":trang}
        return render(request,"product.html",context)
def num_ao(request,numpage):
    if request.method=="POST": # dang nhap
        pass 
    if request.method=="GET":
        count= Products.objects.all().filter(Loai="top").count()
        trang=demtrang(count)
        arr_num_trang= numtrang(numpage)
        start=arr_num_trang[0]
        end=arr_num_trang[1]
        listsp=Products.objects.all().filter(Loai="top")[start:end]
        trang=demtrang(count)
        if request.user.is_authenticated:
            user = request.user
            order, created = Order.objects.get_or_create(user = user,trangthaidonhang="chuaxacnhan")
            items = order.order_product_set.all()
            cartItem = order.tongsanpham
        else:
            items = []
            order={'tongtientatca':0,'tongsanpham':0}
            cartItem = order['tongsanpham']
        context= {'cartItem':cartItem,"order":order,'items':items,"listsp":listsp,"trang":trang}
        return render(request,'product.html',context)

def quan_page(request):
    if request.method=="POST": # dang nhap
        pass 
    if request.method=="GET":
        listsp=Products.objects.all().filter(Loai="bottom")
        count= count= Products.objects.all().filter(Loai="bottom").count()
        trang=demtrang(count)
        trang=demtrang(count)
        if request.user.is_authenticated:
            user = request.user
            order, created = Order.objects.get_or_create(user = user,trangthaidonhang="chuaxacnhan")
            items = order.order_product_set.all()
            cartItem = order.tongsanpham
        else:
            items = []
            order={'tongtientatca':0,'tongsanpham':0}
            cartItem = order['tongsanpham']
        context= {'cartItem':cartItem,"order":order,'items':items,"listsp":listsp,"trang":trang}
        return render(request,"product.html",context)
def num_quan(request,numpage):
    if request.method=="POST": # dang nhap
        pass 
    if request.method=="GET":
        count= count= Products.objects.all().filter(Loai="bottom").count()
        arr_num_trang= numtrang(numpage)
        start=arr_num_trang[0]
        end=arr_num_trang[1]
        listsp=Products.objects.all().filter(Loai="bottom")[start:end]
        return render(request,'product.html',{"listsp":listsp,"trang":trang})

def aokhoac_page(request):
    if request.method=="POST": # dang nhap
        pass 
    if request.method=="GET":
        listsp=Products.objects.all().filter(Loai="coat")
        count= count= Products.objects.all().filter(Loai="coat").count()
        trang=demtrang(count)
        trang=demtrang(count)
        if request.user.is_authenticated:
            user = request.user
            order, created = Order.objects.get_or_create(user = user,trangthaidonhang="chuaxacnhan")
            items = order.order_product_set.all()
            cartItem = order.tongsanpham
        else:
            items = []
            order={'tongtientatca':0,'tongsanpham':0}
            cartItem = order['tongsanpham']
        context= {'cartItem':cartItem,"order":order,'items':items,"listsp":listsp,"trang":trang}
        return render(request,"product.html",context)
def num_aokhoac(request,numpage):
    if request.method=="POST": # dang nhap
        pass 
    if request.method=="GET":
        count= count= Products.objects.all().filter(Loai="coat").count()
        trang=demtrang(count)
        arr_num_trang= numtrang(numpage)
        start=arr_num_trang[0]
        end=arr_num_trang[1]
        listsp=Products.objects.all().filter(Loai="coat")[start:end]
        trang=demtrang(count)
        if request.user.is_authenticated:
            user = request.user
            order, created = Order.objects.get_or_create(user = user,trangthaidonhang="chuaxacnhan")
            items = order.order_product_set.all()
            cartItem = order.tongsanpham
        else:
            items = []
            order={'tongtientatca':0,'tongsanpham':0}
            cartItem = order['tongsanpham']
        context= {'cartItem':cartItem,"order":order,'items':items,"listsp":listsp,"trang":trang}
        return render(request,'product.html',context)
def search_page(request):
    if request.method=="POST": # dang nhap
        pass 
    if request.method=="GET":
        search_data=request.GET.get("search")
        count= listsp=Products.objects.annotate( search=SearchVector('tensp', 'giatien','thuonghieu','Loai')).filter(search=search_data).count()
        trang=demtrang(count)
        listsp=Products.objects.annotate( search=SearchVector('tensp', 'giatien','thuonghieu','Loai')).filter(search=search_data)
        trang=demtrang(count)
        if request.user.is_authenticated:
            user = request.user
            order, created = Order.objects.get_or_create(user = user,trangthaidonhang="chuaxacnhan")
            items = order.order_product_set.all()
            cartItem = order.tongsanpham
        else:
            items = []
            order={'tongtientatca':0,'tongsanpham':0}
            cartItem = order['tongsanpham']
        context= {'cartItem':cartItem,"order":order,'items':items,"listsp":listsp,"trang":trang}
        return render(request,'product.html',context)
def num_search(request,numpage):
    if request.method=="POST": # dang nhap
        pass 
    if request.method=="GET":
        search_data=request.GET.get("search")
        count= listsp=Products.objects.annotate( search=SearchVector('tensp', 'giatien','thuonghieu','Loai')).filter(search=search_data).count()
        trang=demtrang(count)
        arr_num_trang= numtrang(numpage)
        start=arr_num_trang[0]
        end=arr_num_trang[1]
        listsp=Products.objects.annotate( search=SearchVector('tensp', 'giatien','thuonghieu','Loai')).filter(search=search_data)[end:start]
        trang=demtrang(count)
        if request.user.is_authenticated:
            user = request.user
            order, created = Order.objects.get_or_create(user = user,trangthaidonhang="chuaxacnhan")
            items = order.order_product_set.all()
            cartItem = order.tongsanpham
        else:
            items = []
            order={'tongtientatca':0,'tongsanpham':0}
            cartItem = order['tongsanpham']
        context= {'cartItem':cartItem,"order":order,'items':items,"listsp":listsp,"trang":trang}
        return render(request,'product.html',context)
            

def num_search(request,numpage):
    pass
    
        
