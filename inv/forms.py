from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', )

class BookForm(forms.Form):
    product = forms.CharField(max_length=200)
    quantity = forms.IntegerField()
