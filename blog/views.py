from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import MyPublish
from django.utils import timezone
from .forms import PostForm


def index(request):
    posts = MyPublish.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})


def post_info(request, pk):
    post = get_object_or_404(MyPublish, pk=pk)
    return render(request, 'blog/post_info.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})
