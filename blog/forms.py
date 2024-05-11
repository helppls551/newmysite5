from django import forms
from .models import MyPublish


class PostForm(forms.ModelForm):
    class Meta:
        model = MyPublish
        fields = ('title', 'photo', 'phone_number', 'address', 'text', )
