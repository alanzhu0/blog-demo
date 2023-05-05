from django.shortcuts import render, redirect
from .models import Post
from .forms import CreatePostForm

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {
        'posts': Post.objects.all(),
    })


def create_view(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home_view)
        else:
            return redirect(create_view)
    
    context = {
        'form': CreatePostForm(),
    }
    return render(request, 'create.html', context)