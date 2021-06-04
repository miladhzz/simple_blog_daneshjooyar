from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'status',)
    list_filter = ('title', 'author', 'status',)
    search_fields = ('title',)

    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date', 'active',)
    list_filter = ('name', 'email', 'active',)
    search_fields = ('comment',)

