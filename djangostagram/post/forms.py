from django import forms

class WriteForm(forms.Form):
    title = forms.CharField(
        max_length = 100,
        label='제목',
        required=False
    )
    content = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'
        },
        label='내용',
        widget = forms.Textarea()
    )
    img_src = forms.ImageField(
        error_messages={
            'required': '이미지를 입력해주세요.'
        },
        label='이미지'
    )
    tags = forms.CharField(
        label='태그(콤마(,)구분)',
        max_length = 250,
        required=False
    )
