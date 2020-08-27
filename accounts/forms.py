from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Usuário'
        self.fields['email'].label = 'E-mail'
        self.fields['email'].widget.attrs.pop("autofocus", None)
