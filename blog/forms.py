from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    
    class Meta:
        fields = ["title", "content", "time"]
        model = Post