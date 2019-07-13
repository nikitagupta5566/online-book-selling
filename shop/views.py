from django.shortcuts import render,redirect,get_object_or_404
from django.template import loader,context
from django.http import HttpResponse
from django.views.generic import *
from shop.models import *
from django.urls import reverse
from django.contrib.auth.models import User
from shop.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import sqlite3
import datetime

# Create your views here.

class index(TemplateView):
    template_name='index.html'


class UserFormView(CreateView):
    template_name='customerregistration.html'
    model=User
    form_class=UserCreationForm
    success_url='shop'

class customerlogin(View):
    template_name='customerlogin.html'

    def get(self,request):
    	return (render(request,self.template_name,{}))

    def post(self,request):
    	username=request.POST['username']
    	password=request.POST['password']
    	print(username,password)
    	user=authenticate(username=username,password=password)

    	if user is not None:
    		if user.is_active:
    			login(request,user)
    			return (redirect('itemslist'))
    		else:
    			return (render(request,self.template_name,{'errors':'Your account is disabled'}))

    	return (render(request,self.template_name,{'errors':'Invalid UserName or Password','username':username,'password':password}))



class itemdetail(DetailView):
    template_name='bookdetail.html'
    model=Book


class stockregister(ListView):
    template_name='stockregister.html'
    model=Book

def signout(request):
	t=loader.get_template("index.html")
	c={}
	v=t.render(c)
	resp=HttpResponse(v)
	return(resp)


class shopping(ListView):
	template_name='items.html'
	model=Book


def addtocart(request,book_id):
	if request.user.is_authenticated:
		book=get_object_or_404(Book,pk=book_id)
		cart,created=Cart.objects.get_or_create(user=request.user)
		item,created=cartitems.objects.get_or_create(cart=cart,book=book)
		item.quantity+=1
		item.save()
		return (redirect('mycart'))
	else:
		return (render(request,'customerlogin.html',{'message':'Please login into your account first'}))

def mycart(request):
	if request.user.is_authenticated:
		cart=get_object_or_404(Cart,user=request.user)
		items=cartitems.objects.filter(cart=cart)
		return (render(request,'cart.html',{'items':items}))
	else:
		return (render(request,'customerlogin.html',{'message':'Please login into your account first'}))


def removefromcart(request,bookid):
	cart=get_object_or_404(Cart,user=request.user)
	book=get_object_or_404(Book,id=int(bookid))
	cartitems.objects.filter(cart=cart,book=book).delete()
	items=cartitems.objects.filter(cart=cart)
	return (render(request,'cart.html',{'items':items}))


def search(request):
	searchstring=request.GET['q']
	book=Book.objects.filter(name__contains=searchstring)
	return (render(request,'search_results.html',{'book':book}))


		

class placeorder(ListView):

	template_name='myorders.html'

	def get_queryset(self):
		cart=get_object_or_404(Cart,user=self.request.user)
		items=cartitems.objects.filter(cart=cart)

		if items:
			obj=order.objects.create(date=datetime.datetime.now(),status='Received',cart=cart,amount=0)

		x=0
		for item in items:
			cartitems.objects.filter(pk=item.id).delete()
			x=x+item.book.price
			b=Book.objects.get(id=item.book.id)
			b.stock=b.stock-item.quantity
			b.save()
			print(b.stock)
			print(item.book.id)
			
			orderdetail.objects.create(Order=obj,book=item.book,quantity=item.quantity)

		if items:
			obj.amount=x
			obj.save()

		orders=order.objects.filter(cart=cart)
		
		return orders

class myorders(ListView):

	def get_queryset(self):
		cart=get_object_or_404(Cart,user=self.request.user)
		orders=order.objects.filter(cart=cart)
		return orders

	template_name='myorders.html'


class orderdetails(ListView):
	context_object_name='order_list'
	template_name='orderdetail.html'

	def get_queryset(self):
		print(self.kwargs['orderno'])
		orders=order.objects.get(order_no=self.kwargs['orderno'])
		print(orders)
		order_list=orderdetail.objects.filter(Order=orders)
		return order_list

class bookdetails(DetailView):
	template_name='bookdetails.html'
	model=Book

class cancelorder(ListView):

	def get(self,request,orderno):
		obj=order.objects.get(order_no=orderno)
		obj.status='Cancelled'
		obj.save()
		obj=orderdetail.objects.filter(Order=obj)

		for i in obj:
			b=Book.objects.get(id=i.book.id)
			b.stock=b.stock+i.quantity
			b.save()
		return redirect('myorders')


def logout_view(request):
	logout(request)
	return(redirect(reverse('index')))



def changepassword(request):
	resp=HttpResponse()
	return(resp)

#class orderdetails(View):

#	def get(self,orderno):
#		obj=order.objects.get(order_no=orderno)
#		orderdetail=orderdetail.objects.get(order=obj)
#		return (render(request,'orderdetails.html',{'orderdetail':orderdetail}))


	
	
	

