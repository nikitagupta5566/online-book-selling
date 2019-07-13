from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    email=models.EmailField("Email ID",primary_key=True)
    password=models.CharField("Password",max_length=50)
    name=models.CharField("Customer Name",max_length=50)
    address=models.CharField("Address",max_length=100)
    city=models.CharField("City",max_length=50)
    state=models.CharField("State",max_length=50)
    contact=models.IntegerField("Contact Number")

    def __str__(self):
        return self.name

    class Meta():
        verbose_name="Customer"
            

class Book(models.Model):
    name=models.CharField("Item Name",max_length=100)
    price=models.IntegerField("Price")
    stock=models.IntegerField("Stock")
    item_image=models.CharField("Image",max_length=500)
    author=models.CharField("Author",max_length=500,null=True)
    edition=models.IntegerField("Edition",blank=True,null=True)
    Language=models.CharField("Language",max_length=100,null=True)
    Description=models.CharField("Description",max_length=1000,null=True)


    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class cartitems(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)

    def __str__(self):
        return self.book.name

class order(models.Model):
    order_no=models.AutoField(primary_key=True)
    order_status=(
        ('Received','Received'),
        ('Shipped','Shipped'),
        ('Cancelled','Cancelled'),
        ('Delivered','Delivered'),
        )
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    date=models.DateField("Order Date")
    amount=models.IntegerField("Amount")
    status=models.CharField(max_length=20,choices=order_status)

    def __str__(self):
        return str(self.order_no)

class orderdetail(models.Model):
    Order=models.ForeignKey(order,on_delete=models.CASCADE,null=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(null=True)



