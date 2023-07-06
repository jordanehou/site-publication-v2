from django import forms
#from courses.models import Course
# import the default forms models of django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]

class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = [
            'bio',
            'profile_image',
            'type_profile'
        ]
        
        



#class CourseEnrollForm(forms.Form):
#    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.HiddenInput)