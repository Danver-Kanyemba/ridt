from django import forms


class Login(forms.Form):
    Email = forms.CharField(label="Email: ", max_length=100)
    Password = forms.PasswordInput(label="Password: ", max_length=100)

class Register(forms.Form):
    Email = forms.CharField(label="Email: ", max_length=100)
    Password = forms.PasswordInput(label="Password: ", max_length=100)
