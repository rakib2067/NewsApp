from django import forms
import django.forms.utils
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['dob']
        labels = {
        'dob': ('D.O.B'),
        }

        widgets = {
            'dob': forms.DateInput(attrs={'type':'date', 'class': 'form-control'})
        }
 
class ProfileUpdateForm(forms.ModelForm):
     class Meta:
         model=UserProfile
         fields=['image']

class UserUpdateForm(forms.ModelForm):
     class Meta:
         model=UserProfile
         fields=['favourite']
