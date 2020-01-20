from django import forms

class TierForm(forms.Form):
    post = forms.CharField(widget=forms.HiddenInput())
