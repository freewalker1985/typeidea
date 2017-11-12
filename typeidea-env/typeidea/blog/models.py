from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")

    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )

    name = models.CharField(max_length=10, verbose_name='名称')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Post(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
        (3, '草稿'),
    )

    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, related_name='posts', verbose_name='标签')

    content = models.TextField(verbose_name='正文', help_text='正文必须为MarkDown格式')
    owner = models.ForeignKey(User, verbose_name='作者')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def status_show(self):
        return '当前状态:%s' % self.status
    status_show.short_description = '展示状态'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '文章'
