from django.urls import path
from .views import cart, checkout,updateItem,updatequantity,processOrder

urlpatterns = [
    path('cart/',cart,name='cart' ),
    path('checkout/',checkout,name='checkout' ),

    path('updateItem/',updateItem,name='updateItem' ),
    path('updatequantity/',updatequantity,name='updatequantity' ),
    path('processOrder/',processOrder,name='processOrder'),
]
   