from django import forms
from .models import Topic, Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'write your Message',
            'rows': 5,
        }
    ),
        max_length=4000,
        help_text='The Max Length Of The Text Is 4000')

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['message', ]
