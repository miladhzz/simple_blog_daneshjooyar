from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created')
    list_filter = ('title', 'author', 'status', 'created')
    search_fields = ('title', 'body')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('created', 'active')
    search_fields = ('name', 'email')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
