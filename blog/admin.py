from django.contrib import admin
from blog.models import Post, Customer, Seller, Product, Sale

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "create_at")
    list_filter = ("is_published", "create_at")
    search_fields = ("title", "content")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name",'phone', 'email')
    search_fields = ("first_name", "last_name")

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name",'phone', 'email')
    search_fields = ("first_name", "last_name")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name", )

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "customer", "seller", "sale_date", "amount")
    list_filter = ("product", "seller")

