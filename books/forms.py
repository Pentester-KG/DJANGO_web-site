from django import forms
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.AddBooks
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']
