from django import forms
from .models import MyPublish


class PostFrom(forms.ModelForm):
    class Meta:
        model = MyPublish
        fields = ('title', 'photo', 'text')