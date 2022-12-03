from django import forms

class RconQueryForm(forms.Form):
    query = forms.CharField(max_length=512, widget=forms.Textarea(attrs={"rows":5}))