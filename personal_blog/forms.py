from django import forms
from .models import Blog



class AddBlogForm(forms.Form):
    title = forms.CharField(label="标题", max_length=128, widget=forms.TextInput(attrs={'class': 'form-group'}))
    body = forms.CharField(label="内容", widget=forms.Textarea(attrs={'class': 'form-group'}))
