from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib import messages
def dangnhap(username,password,request,redir):
    user = authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        messages.success(request,"đăng nhập thành công")
        return redirect(redir)
    else:
        messages.error(request,"sai tên đăng nhập hoặc mật khẩu")
        
        return redirect(redir)


        