from django import forms


class NewtodoForm(forms.Form):
    todo = forms.CharField(label="New TODO")