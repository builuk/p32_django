from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>", views.post_detail, name="post_detail"),
    path("customers/", views.customer_list, name="customer_list"),
    path("customers/new/", views.customer_create, name="customer_create"),
    path("sellers/", views.seller_list, name="seller_list"),
    path("sellers/new/", views.seller_create, name="seller_create"),
    path("products/", views.product_list, name="product_list"),
    path("products/new/", views.product_create, name="product_create"),
    path("sales/", views.sale_list, name="sale_list"),
    path("sales/new/", views.sale_create, name="sale_create"),
]