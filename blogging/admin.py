from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Post.categories.through
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline
    ]
    exclude = ('categories',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
