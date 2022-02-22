from pydoc import pager
import re
from unicodedata import category, name
from django.shortcuts import get_object_or_404, redirect, render
from matplotlib.pyplot import title
from matplotlib.style import available
# Create your views here.
from store.models import Category, Product,Cart,CartItem
from store.forms import SignUpForm
from django.contrib.auth.models import Group,User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.core.paginator import Paginator,EmptyPage,InvalidPage


def index(request,category_slug=None):
    products= None
    category_page = None
    if category_slug!=None:
        category_page=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.all().filter(category=category_page,available=True)
    else: 
        products= Product.objects.all().filter(available=True)

    paginator = Paginator(products,4)
    try:
       page = int(request.Get.get('page','1'))
    except:
        page = 1
    try:
       productperPage = paginator.page(page)
    except(EmptyPage,InvalidPage):

        productperPage=paginator.page(paginator.num_pages)
    
    return render(request,'index.html',{'products':productperPage,'category':category_page})

def contact(request):
    return render(request,'contact.html')

def series(request):
    return render(request,'series.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def login_(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else :
                return redirect('signup')
    else:
        form = AuthenticationForm()

    return render(request,'login.html',{'form':form})

def signout(request):
    logout(request)
    return redirect('login_')

def signup(request):
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            #บันทึกข้อมูล User
            form.save()
            #บันทึก Group Customer
            #ดึง Username จากแบบฟอร์มมาใช้
            username = form.cleaned_data.get('username')
            #ดึงข้อมูล user มาจากฐานข้อมูล
            signupUser = User.objects.get(username=username)
            #จัด Group 

            customer_group = Group.objects.get(name="Customer")
            customer_group.user_set.add(signupUser)
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})


def product1(request):
    products=None
    products=Product.objects.filter(id=1).only('name')
    return render(request,'product1.html',{'products':products})

def product2(request):
    products=None
    products=Product.objects.filter(id=2).only('name')
    return render(request,'product2.html',{'products':products})

def product3(request):
    products=None
    products=Product.objects.filter(id=3).only('name')
    return render(request,'product3.html',{'products':products})

def product4(request):
    products=None
    products=Product.objects.filter(id=5).only('name')
    return render(request,'product4.html',{'products':products})

def product5(request):
    products=None
    products=Product.objects.filter(id=6).only('name')
    return render(request,'product5.html',{'products':products})

def product6(request):
    products=None
    products=Product.objects.filter(id=7).only('name')
    return render(request,'product6.html',{'products':products})

def product7(request):
    products=None
    products=Product.objects.filter(id=8).only('name')
    return render(request,'product7.html',{'products':products})

def product8(request):
    products=None
    products=Product.objects.filter(id=9).only('name')
    return render(request,'product8.html',{'products':products})

def product9(request):
    products=None
    products=Product.objects.filter(id=10).only('name')
    return render(request,'product9.html',{'products':products})

def product10(request):
    products=None
    products=Product.objects.filter(id=11).only('name')
    return render(request,'product10.html',{'products':products})



def cartDetail(request):
    total = 0
    couter = 0
    cart_items = None

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))#ดึงตระกร้าสินค้า
        cart_items = CartItem.objects.filter(cart=cart,active = True)#ดึงข้อมูลในตระกร้าสินค้า
        for item in cart_items:
            total+=(item.product.price * item.quantity) 
            couter+=item.quantity
    except Exception as e:
        pass
    return render(request,'cartDetail.html',dict(cart_items=cart_items,
    total=total,
    couter = couter))

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def addCart(request,product_id):
    #รหัสสินค้า
    #ดึงสินค้าตามรหัสที่ส่งมา
    product=Product.objects.get(id=product_id)
    #สร้างตระก้าสินค้า
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))

    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _cart_id(request))
        cart.save()

    #ซื้อรายการสินค้าครั้งแรก
    try:
        #ซื้อรายการสินค้า
        cart_item = CartItem.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            #เปลี่ยนจำนวน รายการสินค้า
            cart_item.quantity+=1
            #อัพเดทค่า
            cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity = 1,
        )
        cart_item.save()
    if product_id == 1:
        return redirect('product1')
    if product_id == 2:
        return redirect('product2')
    if product_id == 3:
        return redirect('product3')
    if product_id == 5:
        return redirect('product4')
    if product_id == 6:
        return redirect('product5')
    if product_id == 7:
        return redirect('product6')
    if product_id == 8:
        return redirect('product7')
    if product_id == 9:
        return redirect('product8')
    if product_id == 10:
        return redirect('product9')
    if product_id == 11:
        return redirect('product10')
        
def removeCart(request,product_id):
    #ทำงานกับสินค้าที่จะลบ
    cart =Cart.objects.get(cart_id=_cart_id(request))
    #ทำงานกับสินค้าที่จะลบ
    product = get_object_or_404(Product,id=product_id)
    cartItem = CartItem.objects.get(product=product,cart=cart)
    #ลบรายการสินค้า 1 ออกจากตระกร้า A โดยลบจาก รายการสินค้าในตระกร้า
    cartItem.delete()
    return redirect('cartDetail')

def search(request):
    
    products = Product.objects.filter(name__contains = request.GET['title']).order_by('-id')
    return render(request,'index.html',{'products':products})