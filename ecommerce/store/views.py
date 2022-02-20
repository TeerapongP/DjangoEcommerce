from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
from store.models import Product,Cart,CartItem
import operator


def index(request):
    return render(request,'index.html')



def contact(request):
    return render(request,'contact.html')

def series(request):
    return render(request,'series.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

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
    return redirect('cartDetail')

def removeCart(request,product_id):
    cart =Cart.objects.get(cart_id=_cart_id(request))

    product = get_object_or_404(Product,product_id)
    cartItem = CartItem.objects.get(product=product,cart=cart)