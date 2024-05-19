from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
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
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            print(post.published_date)
            post.save()
            return redirect('post_info', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(MyPublish, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_info', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {"form":form})
