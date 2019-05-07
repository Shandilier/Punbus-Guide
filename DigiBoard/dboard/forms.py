from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Search

class SignUpForm(UserCreationForm):
	class Meta:
		model=User
		fields=('username','first_name','last_name','password1','password2')

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = [
            "source",
            "des",
            "HH",
            "MM"
        ]
