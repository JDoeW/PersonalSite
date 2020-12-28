from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    created = models.DateTimeField(default=timezone.now)
    # auto_now=True 指定每次数据更新写入时间
    updated = models.DateTimeField(auto_now=True)

    # Meta提供元数据, 元数据表示任何不是字段的东西。
    # 比如排序(ordering), 单复数(verbose_name, verbose_name_plural), 数据库表名(db_table)
    # ordering = ('-created') -> created 按创建时间 - 倒序 
    # 在网站首页展示, 最新文章呈现在最上面
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

