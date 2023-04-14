from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta():
        model = Review
        fields = ('title', 'content', 'movie',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label = '',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control'
            },
        ),
    )
    class Meta():
        model = Comment
        fields = ('content',)