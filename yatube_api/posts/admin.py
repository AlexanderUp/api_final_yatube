from django.contrib import admin

from .models import Comment, Follow, Group, Post


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "post", "text", "created",)
    empty_value_display = "-пусто-"


class FollowAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "following",)
    empty_value_display = "-пусто-"


class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "description",)
    empty_value_display = "-пусто-"


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "pub_date", "author", "group", "image",)
    empty_value_display = "-пусто-"


admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
