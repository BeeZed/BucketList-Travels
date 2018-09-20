from django import forms
from .models import UsersModel

# To-Do: Hash password rather than storing in plain text


class LoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}), label='')

    class Meta:
        model = UsersModel
        fields = ('email', 'password')


class SignupForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Name'}))
    email = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    contactno = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Phone Number'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}), label='')
    verify_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Re-type Password'}), label='')

    class Meta:
        model = UsersModel
        fields = ('name', 'email', 'contactno', 'password')

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        verify_password = cleaned_data.get('verify_password')

        if password != verify_password:
            raise forms.ValidationError("Passwords do not match")