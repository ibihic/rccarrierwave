from django import forms

class LoginForm(forms.Form):
    username=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

# class ImageUploadForm(forms.Form):
#     """Image upload form."""
#     image = forms.ImageField()
