from django import forms
from main.models import User


class SignUpForm(forms.ModelForm):
    class Meta:  # Meta - class Meta визначає параметри, що використовуються при побудові форми
        model = User
        fields = ['username', 'email', 'about', 'password']
