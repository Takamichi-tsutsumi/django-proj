from django.contrib import admin
from simpleboard.models import Board, Post, Favorite


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
admin.site.register(Board, BoardAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')
    list_display_links = ('id', )
admin.site.register(Post, PostAdmin)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'post',)
    list_display_links = ('user',)
admin.site.register(Favorite, FavoriteAdmin)