
from django import forms
from crm.models import Students


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model=Students
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.Textarea(attrs={"class":"form-control"}),
            "gender":forms.Select(attrs={"class":"form-select"})
            
        }

        # fields=["name","email","phone","address","gender"]
