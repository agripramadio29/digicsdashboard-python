from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User, Group


# user form
class CreateUserForm(UserCreationForm):

    email = forms.EmailField(max_length=50, required=True)
    # password1 = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)
    # password2 = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CreateUserGroup(UserCreationForm):

#    username = forms.CharField(max_length=50, required=True)
    group = forms.CharField(max_length=10, required=True)

    class Meta:
        model = Group
        fields = ['group']


    def save(self, commit=True):
        group = super(CreateUserGroup, self).save(commit=False)
        group.group = self.cleaned_data['group']
        if commit:
            group.save()
        return group
