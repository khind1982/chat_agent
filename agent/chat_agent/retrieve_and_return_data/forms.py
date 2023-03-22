from django import forms

from retrieve_and_return_data import models

class LazyActiveForm(forms.ModelForm):
    lazy = forms.BooleanField()
    active = forms.BooleanField()

    class Meta:
        model = models.Settings
        fields = ['lazy', 'active']