from django import forms


class CowsayForm(forms.Form):
    cowfield = forms.CharField(max_length=80)
