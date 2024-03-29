from django import forms
from .models import Account, UserProfile


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',

    }))
    passwordconfirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']

    def _init_(self, *args, **kwargs):
        super(RegistrationForm, self)._init_(args, *kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Emaill Address'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Your phone Number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        passwordconfirm = cleaned_data.get('passwordconfirm')

        if password != passwordconfirm:
            raise forms.ValidationError('Passwords dont Match')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        passwordconfirm = cleaned_data.get('passwordconfirm')

        if password != passwordconfirm:
            raise forms.ValidationError('Passwords dont Match')


# user Form for editing and updating
class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone')

    def _init_(self, *args, **kwargs):
        super(UserForm, self)._init_(args, *kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)

    def _init_(self, *args, **kwargs):
        super(UserProfileForm, self)._init_(args, *kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
