from django.urls import path
from . import views

# 部署应用的名称
app_name = 'article'

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
    path('article-detial/<int:id>/', views.article_detail, name='article_detail'),
]
