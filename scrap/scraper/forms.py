from django import forms

class AmazonLinkForm(forms.Form):
    url = forms.URLField(label='Amazon Search Page Url')