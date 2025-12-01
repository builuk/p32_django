from django import forms
from .models import Customer, Seller, Product, Sale

class PostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    content = forms.CharField(label="Content", widget=forms.Textarea)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = "__all__"