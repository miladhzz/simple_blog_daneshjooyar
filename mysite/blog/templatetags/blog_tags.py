from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.all().count()


@register.simple_tag
def tag_label(tag_count):
    if tag_count > 1:
        return 'Tags: '
    else:
        return 'Tag: '
