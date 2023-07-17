from django.urls import path
from .import views
from .views import *


urlpatterns = [
    path("home/", views.home, name="home"),
    path("category-list/", views.category_list, name='category_list'),
    path("add-category/", views.addCategory, name='add_category'),
    path("tag-list/", views.tag_list, name="tag_list"),
    path("product-list/", views.product_list, name='product_list'),
    path('product-list/<pk>/',ProductDetailView.as_view(), name='product_detail'),
    path("add-product/", views.add_product, name='add_product'),
    path("add-tag/", views.add_tag, name='add_tag'),
    path("add-to-cart/<product_id>/", views.add_to_cart, name="add_to_cart"),
    path('cart-list/', views.cart_list, name='cart_list'),
]
