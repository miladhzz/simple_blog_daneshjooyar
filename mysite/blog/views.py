from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator
from . import forms
from taggit.models import Tag


def post_list(request, tag_slug=None):
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = models.Post.objects.filter(status='published',
                                           tags__in=[tag])
    else:
        posts = models.Post.objects.filter(status='published')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    # print(page_number)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    # print(posts)
    return render(request, "post_list.html", context=context)


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(models.Post,
                             created_date__year=year,
                             created_date__month=month,
                             created_date__day=day,
                             slug=slug,
                             status='published')
    # print(post.status)
    comment_form = forms.CommentForm()
    new_comment = None

    if request.method == 'POST':
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    context = {
        'post': post,
        'comment_form': comment_form,
        'new_comment': new_comment,
    }

    return render(request, "post_detail.html", context=context)


def contact_us(request):
    return render(request, "contact_us.html")
