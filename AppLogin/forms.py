from django.forms import ModelForm
from AppLogin.models import User, Profile
from django.contrib.auth.forms import UserCreationForm

#forms

class ProfileForm(ModelForm):
    class meta:
        model = Profile
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')