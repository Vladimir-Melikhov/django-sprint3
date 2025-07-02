from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.const import QUANREST
from blog.models import Category, Post


def get_objects_select_related():
    return Post.objects.select_related(
        "category",
        "author",
        "location",
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )


def index(request):
    posts_lst = (
        get_objects_select_related()
        .order_by("-pub_date")[:QUANREST]
    )
    context = {
        "post_lst": posts_lst,
    }
    return render(request, "blog/index.html", context)


def post_detail(request, post_id):
    posts = get_object_or_404(
        get_objects_select_related().filter(
            pk=post_id,
        )
    )
    context = {"post": posts}
    return render(request, "blog/detail.html", context)


def category_posts(request, category_slug):
    category_obj = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    posts = get_objects_select_related().filter(
        category=category_obj
    ).order_by("-pub_date")
    context = {"category": category_obj, "post_lst": posts}
    return render(request, "blog/category.html", context)
