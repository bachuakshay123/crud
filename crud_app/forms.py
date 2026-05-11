from django import forms
from crud_app.models import student

class studentForms(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Student Name'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Student Email'
            }),
        }