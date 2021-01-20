from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_login(request):
    if 'POST' == request.method:
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data清洗数据
            data = user_login_form.cleaned_data
            # 账户和密码匹配数据库中某一用户数据
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 保存数据到session
                login(request, user)
                return redirect('article:article_list')
            else:
                return HttpResponse('账户和密码输入有误, 请重新输入')
        else:
            return HttpResponse('账户和密码输入不合法')
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse('请使用GET或者POST方法请求数据')


def user_logout(request):
    logout(request)
    return redirect('article:article_list')

