from django.forms import ModelForm, forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from accounts.models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('adress','phone_num','age','email','username','gender_male','gender_female')
        fields = ('adress','phone_num','age','email','username','gender',)

    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username','email','adress','phone_num','age','gender',)



# from django import forms

class VendorRegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser

        fields = (
            'username',
            'email',
            'adress',
            'phone_num',
            'age',
            'gender',
        )
class VendorUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username','email','adress','phone_num','age','gender',)




class VendorLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)