from django import forms

from retrieve_and_return_data import models

class LazyActiveForm(forms.ModelForm):
    lazy = forms.BooleanField()
    active = forms.BooleanField()

    class Meta:
        model = models.Settings
        fields = ['lazy', 'active']

class TemperatureRatingForm(forms.ModelForm):
    cold = forms.BooleanField()
    mild = forms.BooleanField()
    hot = forms.BooleanField()

    class Meta:
        model = models.Settings
        fields = ['cold', 'mild', 'hot']

class LocationForm(forms.ModelForm):
    city = forms.BooleanField()
    mountain = forms.BooleanField()
    sea = forms.BooleanField()

    class Meta:
        model = models.Settings
        fields = ['city', 'mountain', 'sea']