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