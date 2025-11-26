from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(is_published=True).order_by("-create_at")
    context = {"posts": posts}
    return render(request, "blog/post_list.html", context)

def post_detail(request, pk: int):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)