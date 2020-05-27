from django import forms
from .models import Comment

# Comment form class
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add comment...'

    class Meta:
        model = Comment
        fields = ('comments',)