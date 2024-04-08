from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name= 'index'),
    path('cart/',views.cart, name= 'cart'),
    path('deshboard/',views.dashboard, name= 'deshboard'),
    path('order_complete/',views.order_complete, name= 'order_complete'),
    path('place-order/',views.place_order, name= 'place-order'),
    path('product-detail/',views.product_detail, name= 'product-detail'),
    path('register/',views.register, name= 'register'),
    path('search-result/',views.search_result, name= 'search-result'),
    path('signin/',views.sgnin, name= 'signin'),
    path('store/',views.story, name= 'story'),
]

