from django.shortcuts import render, get_object_or_404
from .models import Post, Service


def index(request):
    posts = Post.objects.order_by('-date_added')[:6]
    services = Service.objects.all()
    context = {
        'posts': posts,
        'services': services,
        }
    return render(request, 'home/index.html', context)
