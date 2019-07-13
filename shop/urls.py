from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
    path('registration', views.UserFormView.as_view(), name='registration'),
    path('login', views.customerlogin.as_view(), name='login'),
    path('search', views.search, name='search'),
    path('index', views.index.as_view(),name='index'),
    path('itemdetail/<int:pk>/',views.itemdetail.as_view(),name='bookdetail'),
    path('signout',views.signout,name='signout'),
    path('mycart',views.mycart,name='mycart'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('myorders',views.myorders.as_view(),name='myorders'),
    path('placeorder',views.placeorder.as_view(),name='placeorder'),
    #path('addToCart',views.addToCart,name='addToCart'),
    path('shop',views.shopping.as_view(),name='itemslist'),
    url('addtocart/(?P<book_id>[0-9]+)',views.addtocart,name='addtocart'),
    url('removefromcart/(?P<bookid>[0-9]+)',views.removefromcart,name='removefromcart'),
    path('orderdetails/(?P<orderno>)[0-9]+',views.orderdetails.as_view(),name='orderdetails'),
    path('cancelorder/(?P<orderno>)[0-9]+',views.cancelorder.as_view(),name='cancelorder'),
    path('logout',views.logout_view,name='logout'),
    path('bookdetails',views.bookdetails.as_view(),name='bookdetails'),
]