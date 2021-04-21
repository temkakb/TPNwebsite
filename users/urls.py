from django.urls import path
from django.conf.urls.static import static
from django.conf import settings   
from .views import home,dangky,lienhe,dangxuat,minigame
urlpatterns = [
    
     path('',home,name='home'),
     path('minigame/',minigame,name='minigame'),
     path('logout/',dangxuat,name='logout'),
     path('user/register/',dangky,name='register'),
     path('lienhe/',lienhe,name='lienhe')
     
    
   
]
#urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
