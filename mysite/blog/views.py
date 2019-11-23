from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from taggit.models import Tag

def post_list(request, tag_slug=None):
    object_list = Post.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)
    current_page_number = request.GET.get('page')
    try:
        posts = paginator.page(current_page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'posts': posts,
                                                   'tag': tag})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                 status='published',
                                 created__year=year,
                                 created__month=month,
                                 created__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {'post': post,
                                                     'comments': comments,
                                                     'comment_form': comment_form,
                                                     'new_comment': new_comment})

