from django.shortcuts import render

from .constants import blogs


# Create your views here.
def index(request):
    Post = blogs[:3]
    context = {"Post": Post}
    #return render(request,"soon.html")
    return render(request, "index.html", context)


def blog(request, id):
   
    try:
        Image=False
        Post = next(blog for blog in blogs if blog['id'] == str(id))
        if Post['image']:
            Image=Post['image']
        context = {"Post": Post,"Image":Image}
    
    except Exception as e:
        context = {"Message": e}
    #return render(request,"soon.html")
    return render(request, "blog.html", context)


def allblog(request):
    Post =blogs
    context = {"Post": Post}
    #return render(request,"soon.html")
    return render(request, "allblogs.html", context)
