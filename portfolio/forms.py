from django import forms
from martor.fields import MartorFormField

class SummaryForm(forms.Form):
    summary = MartorFormField()

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'validate',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'validate',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'validate materialize-textarea',
    }))
