from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    posts = models.Post.objects.all()
    # html =  ""
    # for post in posts:
    #     html = html+"<li>"+post.title+"</li>"
    # return HttpResponse("<ol>"+ html +"</ol>")
    return render(request, 'index.html', { "posts" : posts})