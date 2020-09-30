from django.contrib import admin

from .models import Comment, Post


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
