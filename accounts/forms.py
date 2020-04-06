from django import forms 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class ProfileForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    
