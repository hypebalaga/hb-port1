from django.shortcuts import render

from .models import Blog


# Create your views here.
def index(request):
    Post = Blog.objects.order_by("-created_at")[:3]
    context = {"Post": Post}
    return render(request, "index.html", context)


def blog(request, id):
    try:
        Post = Blog.objects.get(id=id)
        context = {"Post": Post}
    except Blog.DoesNotExist:
        context = {"Message": "No blog post found with ID {}".format(id)}
    except Exception as e:
        context = {"Message": e}
    return render(request, "blog.html", context)


def allblog(request):
    Post = Blog.objects.all()
    context = {"Post": Post}
    return render(request, "allblogs.html", context)
