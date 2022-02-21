from django.contrib import admin
from django.urls import path
from store import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('contact/', views.contact, name='contact'),
    path('series/', views.series, name='series'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('login_/', views.login_, name='login_'),
    path('signup/', views.signup, name='signup'),
    path('cartDetail/', views.cartDetail, name='cartDetail'),
    path('cart/add/<int:product_id>', views.addCart, name='addCart'),
    path('cart/remove/<int:product_id>', views.removeCart, name='removeCart'),

    path('product1/',views.product1,name='product1'),
    path('product2/',views.product2,name='product2'),
    path('product3/',views.product3,name='product3'),
    path('product4/',views.product4,name='product4'),
    path('product5/',views.product5,name='product5'),
    path('product6/',views.product6,name='product6'),
    path('product7/',views.product7,name='product7'),
    path('product8/',views.product8,name='product8'),
    path('product9/',views.product9,name='product9'),
    path('product10/',views.product10,name='product10'),

]

if settings.DEBUG :
    urlpatterns+=static(settings.MEDIA_URL,documnet_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,documnet_root=settings.STATIC_ROOT)