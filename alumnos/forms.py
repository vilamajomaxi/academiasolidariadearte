from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=50, widget=forms.TextInput(
            attrs={'placeholder': 'Ingrese su usuario', 'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
            attrs={'placeholder': 'Ingrese su password', 'class': 'form-control'}))
