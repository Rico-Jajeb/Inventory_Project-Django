from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signup_user_form(UserCreationForm):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'itmInput_update new_cont text-light', }))
    last_name  = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'itmInput_update new_cont text-light  ', }))
    email     = forms.EmailField(widget=forms.EmailInput(attrs={'class':'itmInput_update text-light new_cont ', }))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class':'itmInput_update new_cont text-light  ', }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'itmInput_update new_cont text-light  ', }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'itmInput_update new_cont text-light  ', }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(signup_user_form, self).__init__(*args, **kwargs)

        # self.fields['username'].widget.attrs['class'] = 'itmInput_update text-light'
        # self.fields['password1'].widget.attrs['class'] = 'itmInput_update text-light'
        
        # self.fields['password2'].widget.attrs['class'] = 'itmInput_update text-light'

        # widgets = {
 
        #     'first_name': forms.TextInput(attrs={'class':'itmInput_update', }),
        #     'last_name': forms.TextInput(attrs={'class':'itmInput_update', }),
        #     'email': forms.EmailInput(attrs={'class':'itmInput_update', }),
        #     'username': forms.TextInput(attrs={'class':'itmInput_update', }),
        #     'password1': forms.TextInput(attrs={'class':'itmInput_update', }),
        #     'password2': forms.TextInput(attrs={'class':'itmInput_update', }),

        # }