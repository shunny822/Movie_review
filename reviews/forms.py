from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    title  = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control mb-4',
            }
        )
    )

    content = forms.CharField(
        label = '내용',
        widget = forms.Textarea(
            attrs={
                'class': 'form-control mb-4',
            }
        )
    )

    movie  = forms.CharField(
        label = '영화 제목',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control mb-4',
            }
        )
    )

    class Meta():
        model = Review
        fields = ('title', 'content', 'movie',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label = '',
        widget = forms.TextInput(
            attrs={
                'placeholder' : '댓글 작성',
                'class': 'form-control',
            },
        ),
    )
    class Meta():
        model = Comment
        fields = ('content',)


    