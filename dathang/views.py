from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from sanpham.models import Products

# Create your views here.
@login_required(login_url='home')
def cart(request):
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
        context= {'cartItem':cartItem,"order":order,'items':items}
        return render(request, 'cart.html',context)
@login_required(login_url='home')
def checkout(request):
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
    return render(request, 'checkout.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    size = data['Size']
    print('Action:',action)
    print('ProductId:',productId)
    user = request.user
   
    product=Products.objects.get(masp=productId)
    order, created = Order.objects.get_or_create(user = user ,trangthaidonhang="chuaxacnhan")
   
    orderItem, created = Order_Product.objects.get_or_create(order=order,Product=product,Size=size)
    if action =='add':
        orderItem.quantity=(orderItem.quantity+1)
        orderItem.save()
    elif action=='remove':
        orderItem.delete()
    
    if orderItem.quantity<=0:
        orderItem.delete()  

    return JsonResponse('Item was added', safe=False)
def updatequantity(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    quantity=data['Quantity']
    user = request.user
    product=Products.objects.get(masp=productId)
    order, created = Order.objects.get_or_create(user = user ,trangthaidonhang="chuaxacnhan")
    orderItem, created = Order_Product.objects.get_or_create(order=order,Product=product)
    
    orderItem.quantity_change(int(quantity))
    orderItem.save()
    return JsonResponse('change thanh cong', safe=False)
def processOrder(request):
    data=json.loads(request.body) # lay data body

    user = request.user
    order, created = Order.objects.get_or_create(user = user ,trangthaidonhang="chuaxacnhan") # lay order chua xac nhan
    total=data['Shipping']['total']
    listproduct=Order_Product.objects.all().filter(order=order)
    for item in listproduct:
        item.Product.soluongtonkho=item.Product.soluongtonkho-item.quantity
        item.Product.save()
    order.trangthaidonhang="daxacnhan"
    order.tongtien=total
    order.save()
    diachigiaohang.objects.create(
        order=order,diachi=data['Shipping']['address'],
        ten=data['Shipping']['Fname'],
        email=data['Shipping']['Email'],
        ho=data['Shipping']['Lname'],
        quan=data['Shipping']['district'],
        loinhan=data['Shipping']['text'],
        sdt=data['Shipping']['phonenumber']
    )


    return JsonResponse("payment complete",safe=False)





