from django.shortcuts import render
from django.http import Http404
from .models import Post

# Posts view function
def posts(request):
    posts = Post.objects.order_by('-pk')
    return render(
        request,
        'posts/posts.html',
        {
            "posts": posts,
        }
    )

# Article view function
def article(request, postId):
    try:
        article = Post.objects.get(id=postId)
    except DoesNotExist:
        raise Http404()
    return render(
        request,
        'posts/article.html',
        {
            "article": article,
        }
    )