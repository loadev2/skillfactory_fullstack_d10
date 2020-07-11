from django import forms

class FormFilter(forms.Form):
    searchText = forms.CharField(label="", max_length=30)
