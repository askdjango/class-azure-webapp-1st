from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import CommentForm


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post_list': post_list})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', {
        'post': post,
        'form': form,
    })

