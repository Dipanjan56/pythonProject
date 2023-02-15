from django import forms
from .models import Review
from django.forms import ModelForm


# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.CharField(label='Email')
#     review = forms.CharField(label='Please write your review here', widget=forms.Textarea(attrs={'class': 'myform'}))


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        """if we want specific field to be stored form model in html"""
        # fields = ['first_name', 'last_name', 'stars']

        """if we want all the fields to be stored form model in html"""
        fields = '__all__'

        """if you different names to be shown in html form as compared to model"""
        labels = {
            'first_name': 'YOUR FIRST NAME',
            'last_name': 'YOUR LAST NAME',
            'stars': 'RATING',
        }

        # custom messages fpr error
        error_messages = {
            'stars': {
                'min_value': 'Yo! Min Value is 1',
                'max_value': 'Yo! Max Value is 5',
            }
        }
