import markdown
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost
from .forms import ArticleForm
from django.contrib.auth.models import User

# Create your views here.

def article_list(request):
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    return render(request, 'article/list.html', context)


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
        extensions=[
        # 语法、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
    ])
    context = {'article': article}
    return render(request, 'article/detail.html', context)


def article_create(request):
    if 'POST' == request.method:
        article_post_form = ArticleForm(data=request.POST)
        # 提交数据满足ArticleForm模型要求
        if article_post_form.is_valid():
            # 保存数据暂时不提交数据库
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=1)
            # 文章保存到数据库
            new_article.save()
            return redirect('article:article_list')
        else:
            return HttpResponse('表单内容有误, 请重新输入')
    else:
        article_post_form = ArticleForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html', context)


def article_safe_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect('article:article_list')


def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    if 'POST' == request.method:
        article_post_form = ArticleForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect('article:article_list', id=id)
        else:
            return HttpResponse('表单内容有误, 请重新输入')
     else:
        article_post_form = ArticleForm()
        context = {'article': article, 'article_post_form': article_post_form}
        return render(request, 'article/update.html', context)

