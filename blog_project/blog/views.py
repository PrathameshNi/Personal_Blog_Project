from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST' and request.user.is_authenticated:
        text = request.POST.get('comment')
        Comment.objects.create(post=post, user=request.user, text=text)

    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('post_detail', slug=slug)
