from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class LocationAddForm(forms.Form):
    bno = forms.CharField(max_length=100)
    street = forms.CharField(max_length=100)
    area = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    
