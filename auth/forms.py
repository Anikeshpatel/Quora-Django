from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs= {
            "placeholder": "Email"
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs= {
            "placeholder": "Password"
        }))


class SignupForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs= {
            "placeholder": "Name"
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs= {
            "placeholder": "Email"
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs= {
            "placeholder": "Password"
        }))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs= {
            "placeholder": "Password"
        }))