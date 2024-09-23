from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget

 

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'author', 'body']
        
        widgets = {
                    'title': forms.TextInput(
                        attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
                    ),
                    'author': forms.Select(
                        attrs={'class': 'custom-select'},
                    ),
                    'content': SummernoteWidget(),
        }