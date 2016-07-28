from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from .models import Post
import time

# Create your views here.

def index(request):
    t = time.time()
    posts = models.Post.objects.all()
    # html =  ""
    # for post in posts:
    #     html = html+"<li>"+post.title+"</li>"
    # return HttpResponse("<ol>"+ html +"</ol>")
    tme = time.time()-t
    return render(request, 'posts/index.html', {"posts" : posts, "time" : tme})


def details(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/details.html', {'post': post})