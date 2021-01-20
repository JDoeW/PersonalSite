# -*- coding:utf-8 -*-
from django import forms


# forms.Form适用于不与数据库交互
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


# 继承forms.ModelForm, 在Meta辅助类中, 从模型创建Form类, 表单会生成已有字段
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2')
            return data.get('password')
        else:
            return forms.ValidationError('两次密码输入不一致, 请重试!')

