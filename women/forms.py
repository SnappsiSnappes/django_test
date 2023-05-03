import attrs
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import BoundField
# from captcha.fields import CaptchaField
from ckeditor.widgets import CKEditorWidget

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label='Категория не выбрана'
    class Meta:
        model=Women

        fields=['title','content','photo','price','old_price', 'is_published','cat']
        widgets= {
            'title':forms.TextInput(attrs={'class':'form-control fs-4'}),
            'content':forms.Textarea(attrs={'class':' form-control fs-4'}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'id': 'id_price'}),
            'old_price': forms.NumberInput (attrs={'id':'id_old_price'}),
            'is_published':forms.CheckboxInput(attrs={'class':'form-check-input  w-auto p-3 ms-1 form-check'}),
            'cat':forms.Select(attrs={'class':'-auto p-3','id': 'id_category'})
        }
    def clean_title(self):
        title=self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title

    def clean(self):

        cleaned_data = super().clean()
        category = cleaned_data.get('cat')
        price = cleaned_data.get('price')
        print(category)
       #if category.id == 2 and not price:
       #    raise forms.ValidationError("Please provide a price for the selected item.")
       #return cleaned_data



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model=User
        fields=('username','email','password1','password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # captcha = CaptchaField()