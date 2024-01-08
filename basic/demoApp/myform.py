from django import forms

class Login(forms.Form):
    Name = forms.CharField(max_length=25)
    Email = forms.EmailField()