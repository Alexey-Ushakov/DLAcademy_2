from django import forms

from advito.models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'price', 'image', 'category']

        labels = {
            'title': 'Название',
            'description': 'Описание'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),

        }