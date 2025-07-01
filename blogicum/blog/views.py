from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category


def index(request):
    posts_lst = (
        Post.objects.select_related("category", "author", "location")
        .filter(is_published=True, category__is_published=True,
                pub_date__lte=timezone.now())
        .order_by("-pub_date")[:5]
    )
    context = {
        "post_lst": posts_lst,
    }
    return render(request, "blog/index.html", context)


def post_detail(request, post_id):
    posts = get_object_or_404(
        Post.objects.select_related("category", "author", "location").filter(
            pk=post_id, is_published=True, category__is_published=True,
            pub_date__lte=timezone.now()
        )
    )
    context = {"post": posts}
    return render(request, "blog/detail.html", context)


def category_posts(request, category_slug):
    categories = get_object_or_404(Category, slug=category_slug,
                                   is_published=True)
    posts = (
        Post.objects.select_related("category", "author", "location")
        .filter(category__slug=category_slug, is_published=True,
                pub_date__lte=timezone.now())
        .order_by("-pub_date")
    )
    context = {"category": categories, "post_lst": posts}
    return render(request, "blog/category.html", context)
