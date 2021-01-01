from django import forms
from .models import ArticlePost


class ArticleForm(forms.ModelForm):
    class Meta:
        # 指定数据模型来源
        model = ArticlePost
        # 定义表单包含字段, created、updated字段自动生成, author默认指定为id=1的用户
        fields = ('title', 'body')

