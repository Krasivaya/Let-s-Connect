from django.shortcuts import render
from .models import Post

# Posts view function
def posts(request):
    posts = Post.objects.all()
    return render(
        request,
        'posts/posts.html',
        {
            "posts": posts,
        }
    )