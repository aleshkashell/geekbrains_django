from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django import forms
import re
from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        match = re.match(r'^[a-zA-Z0-9]+[a-zA-Z0-9._-]*@[a-zA-Z0-9]+([a-zA-Z0-9._-]+\.)[a-zA-Z0-9]+$', data)
        if not match:
            raise forms.ValidationError("Некорректный email адрес")
        return data


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        match = re.match(r'^[a-zA-Z0-9]+[a-zA-Z0-9._-]*@[a-zA-Z0-9]+([a-zA-Z0-9._-]+\.)[a-zA-Z0-9]+$', data)
        if not match:
            raise forms.ValidationError("Некорректный email адрес")
        return data
