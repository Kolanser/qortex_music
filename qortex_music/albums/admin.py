from django.contrib import admin

from .models import Album, AlbumSing, Sing, Singer


@admin.register(AlbumSing)
class AlbumSing(admin.ModelAdmin):
    """Админка для связи альбомов и песен."""
    list_display = (
        'album',
        'sing',
        'number_sing',
    )
    search_fields = ('sing',)
    list_filter = ('album',)


@admin.register(Album)
class Album(admin.ModelAdmin):
    """Админка для альбомов."""
    list_display = (
        'id',
        'name',
        'year',
        'singer',
    )
    search_fields = ('name',)
    list_filter = ('year', 'singer')


@admin.register(Sing)
class Sing(admin.ModelAdmin):
    """Админка для альбомов."""
    list_display = (
        'id',
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Singer)
class Singer(admin.ModelAdmin):
    """Админка для альбомов."""
    list_display = (
        'id',
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)
