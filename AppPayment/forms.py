from django import forms
from AppPayment.models import BillingAddress
from django.forms import ModelForm


class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ('address', 'zipcode', 'city', 'country',)