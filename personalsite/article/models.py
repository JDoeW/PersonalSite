from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateTimeField(default=timezone.now)
	# auto_now=True 指定每次数据更新写入时间
	updated = models.DateTimeField(auto_now=True)

	class Meta:
	    ordering = ('-created',)

	class __str__(self):
	    return self.title

