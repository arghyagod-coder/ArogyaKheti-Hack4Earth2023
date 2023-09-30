from django import forms
from phonenumber_field.formfields import PhoneNumberField

class RegisterFIDC(forms.Form):
    name = forms.CharField(label="Your Name",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name'
        }),max_length=200)
    phone = PhoneNumberField(label="Phone Number", region='IN', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': '(123) 456-7890'
        }))
    address = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your address (optional)',
        }))
    pincode = forms.IntegerField(label="Area PIN Code", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your location zipcode'
        }))
    farmname = forms.CharField(label="Name of your Farm",max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name of your Farm'
        }))
    farmlandmarks = forms.CharField(label="Landmarks (e.g. near police station, near post office, etc.)",max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nearby Landmarks'
        }))
    farmarea = forms.DecimalField(label="Area of your farm (in hectares)",max_digits=10000, decimal_places=3, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Area of your farm in hectares'
        }))
    
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Tell us more about yourself (optional)',
        }))
    
class LoginWithFIDC(forms.Form):
    name = forms.CharField(label="Your Name",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name'
    }),max_length=200)
    fidcId = forms.CharField(label="FIDC Number",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name'
    }),max_length=200)