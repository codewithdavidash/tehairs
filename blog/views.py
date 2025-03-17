from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import (
    Comment,
    Blog,
)
from .forms import CommentForm


def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog
    }
    return render(request, 'blog/index.html', context)


def blog_details(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.created_by = request.user
            x.blog = blog
            x.save()
            return redirect('blog_details', slug=slug)

    else:
        form = CommentForm()
    context = {
        'blog': blog,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog/details.html', context)
