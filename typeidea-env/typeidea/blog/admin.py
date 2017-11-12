from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .adminforms import PostAdminForm
from .models import Post, Category, Tag
from typeidea.custom_site import custom_site


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

    list_display = [
        'title', 'category', 'status_show', 'created_time', 'operator'
    ]
    list_display_links = []

    list_filter = ['category', ]
    search_fields = ['title', 'category__name']
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True

    fieldsets = (
        ('基础配置', {
            'fields': (('category', 'title'), 'desc', 'status', 'content')
        }),
        ('高级配置', {
            'fields': ('tags', ),
        }),
    )

    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>',
                           reverse(
                               'cus_admin:blog_post_change', args=(obj.id,)))

    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)


class PostInlineAdmin(admin.StackedInline):
    fields = ('title', 'status')
    max_num = 4
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        PostInlineAdmin,
    ]


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass