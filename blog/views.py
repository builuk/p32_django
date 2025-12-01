from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Customer, Seller, Product, Sale
from .forms import PostForm, CustomerForm, SellerForm, ProductForm, SaleForm
def post_list(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
                is_published=False,
            )
            return redirect("blog:post_list")
    else:
        form = PostForm()
    posts = Post.objects.filter(is_published=True).order_by("-create_at")
    context = {"posts": posts, "form": form}
    return render(request, "blog/post_list.html", context)

def post_detail(request, pk: int):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "blog/customer_list.html", {"customers": customers})

def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:customer_list")
    else:
        form = CustomerForm()
    return render(request, "blog/customer_form.html", {"form": form})

def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, "blog/seller_list.html", {"sellers": sellers})

def seller_create(request):
    if request.method == "POST":
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:seller_list")
    else:
        form = SellerForm()
    return render(request, "blog/seller_form.html", {"form": form})

def product_list(request):
    products = Product.objects.all()
    return render(request, "blog/product_list.html", {"products": products})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:product_list")
    else:
        form = ProductForm()
    return render(request, "blog/product_form.html", {"form": form})

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, "blog/sale_list.html", {"sales": sales})

def sale_create(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:sale_list")
    else:
        form = SaleForm()
    return render(request, "blog/sale_form.html", {"form": form})