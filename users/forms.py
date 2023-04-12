from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    security_question = forms.ChoiceField(choices=[
        ('What was the name of your first pet?', 'What was the name of your first pet?'),
        ('In what city were you born?', 'In what city were you born?'),
        ("What is your mother's maiden name?", "What is your mother's maiden name?"),
        ('What was the name of your first school?', 'What was the name of your first school?'),
        ('What is your favorite color?', 'What is your favorite color?')
    ])
    security_answer = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'security_question', 'security_answer']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'full_name',
            'image',
            'date_of_birth',
            'address',
            'city_town',
            'country',
            'security_question',  
            'security_answer'  
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()

