
from django import forms
from crm.models import Students

from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]





class StudentCreateForm(forms.ModelForm):
    class Meta:
        model=Students
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.Textarea(attrs={"class":"form-control","rows":3}),
            "gender":forms.Select(attrs={"class":"form-select"}),

            
        }

        # fields=["name","email","phone","address","gender"]
