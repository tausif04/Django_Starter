from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        exclude = ['user']
        widgets = {
            'image' : forms.FileInput(),
            'displayname' : forms.TextInput(attrs={'placeholder': 'Add to display name'}),
            'info' : forms.Textarea(attrs={'rows':3,'placeholder':'Add information'}),
        }                   

class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']