from django import forms
from movies.models import Reviews


class ReviewFrom(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text', 'parent')
