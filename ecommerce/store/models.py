from distutils.command.upload import upload
from pyexpat import model
from tabnanny import verbose
from unicodedata import category, name
from django.db import models
from django.forms import CharField



class Category(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=('name',)
        verbose_name='หมวดหมู่สินค้า'
        verbose_name_plural='ข้อมูลประเภทหนังสือ'
        

class Product(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="product",blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=('name',)
        verbose_name='หนังสือ'
        verbose_name_plural='ข้อมูลหนังสือ'

class Cart(models.Model):
    cart_id = models.CharField(max_length=255,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.cart_id

    class Meta:
        db_table ='cart'
        ordering = ('date_added',)
        verbose_name='ตระกร้าสินค้า'
        verbose_name_plural='ข้อมูลตระกร้าสินค้า'

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table ='cartItem'
        verbose_name='รายการสินค้าในตระกล้า'
        verbose_name_plural='ข้อมูลรายการสินค้าในตระกล้า'
        
    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name