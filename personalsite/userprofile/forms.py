# -*- coding:utf-8 -*-
from django import forms


# forms.Form适用于不与数据库交互
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

