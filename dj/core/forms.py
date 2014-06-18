from django import forms
from dj.core import models

class LocalForm(forms.ModelForm):
    class Meta:
        model = models.Local
        fields = ['name', 'address']

class CommentForm(forms.ModelForm):
#   date = forms.DateField(
#       widget=forms.DateInput(format='%d/%m/%Y'),
#       input_formats=['%d/%m/%y','%d/%m/%Y'])
    class Meta:
        model = models.Comment

