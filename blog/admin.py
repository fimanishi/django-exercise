from django.contrib import admin
from blog.models import Blog, Post, Poll, Choice
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'created', 'blog')
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'slug')
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('answer', 'count')
