from django import forms
from django.contrib.auth.hashers import check_password
from .models import Dsuser

class RegisterForm(forms.Form):
    id = forms.CharField(
        error_messages={
            'required': '모든 값을 입력해야 합니다.'
        },
        max_length=128,
        label='아이디'
    )
    email = forms.EmailField(
        error_messages={
            'required': '모든 값을 입력해야 합니다.'
        },
        max_length=255, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '모든 값을 입력해야 합니다.'
        },
        max_length=128,
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '모든 값을 입력해야 합니다.'
        },
        max_length=128,
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()
        id = cleaned_data.get('id')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')

        try:
            Dsuser.objects.get(id=id)
            self.add_error('id', '이미 가입된 아이디입니다.')
        except Dsuser.DoesNotExist:
            pass

class LoginForm(forms.Form):
    id = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=128,
        label='아이디'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        id = cleaned_data.get('id')
        password = cleaned_data.get('password')

        if id and password:
            try:
                user = Dsuser.objects.get(id=id)
            except Dsuser.DoesNotExist:
                self.add_error('id', '등록된 아이디가 없습니다')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다')