from django.http import HttpResponse
from django.shortcuts import render
from .models import MyPublish
from django.utils import timezone


def index(request):
    posts = MyPublish.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})



def categ(request, catid):
    return HttpResponse(f"<h1>Cats{catid}</h1>")

def widh(request):
    return render(request,'blog/widh.html ')
def detail(request):
    return render(request,'blog/detail.html')


