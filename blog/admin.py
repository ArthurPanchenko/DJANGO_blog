from django.contrib import admin
from .models import Post, Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')

admin.site.register(Profile)