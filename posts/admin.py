from django.contrib import admin

from .models import Post, PostFile


class PostFileInline(admin.StackedInline):
    model = PostFile
    fields = ('file', )
    extra = 0
    can_delete = False


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_active', 'created_at')
    inlines = (PostFileInline,)


admin.site.register(Post, PostAdmin)