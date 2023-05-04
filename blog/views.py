from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {
        'posts': Post.objects.all(),
    })


def create_view(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    post = Post.objects.create(title=title, content=content)
    post.save()
    return redirect('home')