from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    return render(request, 'le_posts/post_list.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'le_posts/post_list.html', {'posts': posts})