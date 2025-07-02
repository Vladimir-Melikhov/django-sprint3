from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post
from blog.const import QUANREST


def get_object():
    return Post.objects.select_related(
        "category",
        "author",
        "location",
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
    )


def index(request):
    posts_lst = (
        get_object()
        .filter(category__is_published=True)
        .order_by("-pub_date")[:QUANREST]
    )
    context = {
        "post_lst": posts_lst,
    }
    return render(request, "blog/index.html", context)


def post_detail(request, post_id):
    posts = get_object_or_404(
        get_object().filter(
            pk=post_id,
            category__is_published=True,
        )
    )
    context = {"post": posts}
    return render(request, "blog/detail.html", context)


def category_posts(request, category_slug):
    category_obj = get_object_or_404(Category, slug=category_slug, 
                                     is_published=True)
    posts = get_object().filter(category=category_obj).order_by("-pub_date")
    context = {"category": category_obj, "post_lst": posts}
    return render(request, "blog/category.html", context)
