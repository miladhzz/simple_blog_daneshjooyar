from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'status',)
    list_filter = ('title', 'author', 'status',)
    search_fields = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date', 'active',)
    list_filter = ('name', 'email', 'active',)
    search_fields = ('comment',)


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)
