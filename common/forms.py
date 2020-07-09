from django import forms

class FormFilter(forms.Form):
    searchText = forms.CharField(label="Search", max_length=30)
