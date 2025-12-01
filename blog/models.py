from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.content}"

class Customer(models.Model):
    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200)
    phone = models.CharField('Phone',max_length=200)
    email = models.EmailField("Email", unique=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Seller(models.Model):
    class Position(models.TextChoices):
        SELLER = 'SELLER', 'Seller'
        HEAD_SELLER = 'HEAD_SELLER', 'Head Seller'
        MANAGER = 'MANAGER', 'Manager of sellers'

    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200)
    phone = models.CharField('Phone', max_length=200)
    email = models.EmailField("Email", unique=True)
    hire_date = models.DateField("Hire Date", auto_now_add=True)
    position = models.CharField('Position', max_length=20, choices=Position.choices, default=Position.SELLER)
    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

    def __str__(self):
        return f"{self.first_name} {self.last_name} "

class Product(models.Model):
    name = models.CharField('Title', max_length=200)
    description = models.TextField()
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.name}"

class Sale(models.Model):
    customer = models.ForeignKey(Customer,verbose_name='customer', on_delete=models.CASCADE,related_name='sales')
    seller = models.ForeignKey(Seller,verbose_name='seller', on_delete=models.PROTECT,related_name='sales')
    product = models.ForeignKey(Product, verbose_name='product', on_delete=models.PROTECT, related_name='sales')
    sale_date = models.DateField('date', auto_now_add=True)
    amount = models.DecimalField('Amount', max_digits=10, decimal_places=2)
    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
    def __str__(self):
        return f"{self.sale_date} {self.product} -> {self.customer}"