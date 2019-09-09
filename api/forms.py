from django import forms
from . import models

class addPerson(forms.Form):
    fname = forms.CharField(max_length=30, required=True)
    lname = forms.CharField(max_length=30, required=True)
    patronymic = forms.CharField(max_length=30)
    old = forms.IntegerField()

class addWork(forms.Form):
    person_id = forms.IntegerField(required=True)
    pay = forms.IntegerField(required=True)