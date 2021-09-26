from django.contrib import admin

from .models import Post, Group, Comment, Follow

empty_value = '-пусто-'


class SiteAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(SiteAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = empty_value


@admin.register(Group)
class GroupAdmin(SiteAdmin):
    list_display = ('title', 'slug', 'description')
    search_fields = ('title',)
    empty_value_display = empty_value


@admin.register(Comment)
class CommentAdmin(SiteAdmin):
    list_display = ('pk', 'post', 'author', 'text', 'created')
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = empty_value


@admin.register(Follow)
class FollowAdmin(SiteAdmin):
    list_display = ('user', 'author')
    search_fields = ('author',)
    list_filter = ('author',)
    empty_value_display = empty_value
