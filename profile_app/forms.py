from django import forms
from django.contrib.auth.forms import UserCreationForm
from profile_app.models import Profile
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'contacts', 'biography', 'birth_date']
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'}),
            'contacts': PhoneNumberPrefixWidget(),
        }
