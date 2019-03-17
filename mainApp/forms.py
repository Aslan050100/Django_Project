from django import forms
from .models import *

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ["name", "email"]