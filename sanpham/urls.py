from django.urls import path
from .views import sanpham_page,chitietsp,num_sanpham,ao_page,aokhoac_page,quan_page,num_quan,num_ao,num_aokhoac
from .views import search_page,num_search
urlpatterns = [
  
  path('',sanpham_page,name='sanpham_page'),
  path('id/<str:id>/',chitietsp,name="chitietsp"),
  path('<int:numpage>/',num_sanpham,name='num_sanpham'),
  path('ao/',ao_page,name='ao_page'),
  path('ao/<int:numpage>/',num_ao,name='num_ao'),
  path('quan/',quan_page,name='quan_page'),
  path('quan/<int:numpage>/',num_quan,name='num_quan'),
  path('aokhoac/',aokhoac_page,name='aokhoac_page'),
  path('aokhoac/<int:numpage>/',num_aokhoac,name='aokhoac_page'),
  path('search/',search_page,name="search_page"),
  path('search/<int:numpage>/',num_search,name='num_search'),
  
  
   
    
    
]