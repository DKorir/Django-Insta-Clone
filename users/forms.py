from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from theinsta.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_image','website_url','facebook_url','twitter_url','instagram_url','pinterest_url')


        widgets = {
            'bio':forms.Textarea(attrs={'class': 'form-control'}),
            # 'profile_image':forms.ImageField(attrs={'class': 'form-control'}),
            'website_url':forms.TextInput(attrs={'class': 'form-control'}),  
            'facebook_url':forms.TextInput(attrs={'class': 'form-control'}),  
            'twitter_url':forms.TextInput(attrs={'class': 'form-control'}),  
            'instagram_url':forms.TextInput(attrs={'class': 'form-control'}),  
            'pinterest_url':forms.TextInput(attrs={'class': 'form-control'}),      
        }


class SignUpForm(UserCreationForm):
    email =forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    def __init__(self,  *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'