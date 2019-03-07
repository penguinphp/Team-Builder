from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Profile


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'first_name', 'last_name',
                  'password1', 'password2',)


class EditProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=False)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password',)


class AvatarForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('avatar', )


class SkillForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('skills', )
