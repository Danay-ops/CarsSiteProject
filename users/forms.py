from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='login')
    password =forms.CharField(label='password', widget=forms.PasswordInput)
    password2=forms.CharField(label='repeat password', widget=forms.PasswordInput)
    class Meta:
        model = get_user_model()
        fields = ['username','email', 'first_name', 'last_name', 'password','password2']
        labels={
            'email': 'E-mail',
            'first_name' : 'First name',
            'last_name' : 'Last name'
        }
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Second password is wrong')
        else:
            return cd['password']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('That email already in')
        else:
            return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail    ', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'})
        }

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль",widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Новый пароль",widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Повторить новый пароль",widget=forms.PasswordInput)

