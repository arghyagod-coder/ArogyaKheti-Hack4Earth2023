from django import forms

SOIL_TYPES =  [
    ('Sandy', 'Sandy'),
    ('Loamy', 'Loamy'),
    ('Clayey', 'Clayey'),
    ('Red', 'Red'),
    ('Black', 'Black'),
    ]

class CropRecommendationForm(forms.Form):
    nitrogen = forms.IntegerField(label="Soil Nitrogen (N) Content",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your soil nitrogen content'
        }))
    phosphorus = forms.IntegerField(label="Soil Phosphorus (P) Content",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your soil phosphorus content'
        }))
    potassium = forms.IntegerField(label="Soil Potassium (K) Content",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your soil potassium content'
        }))
    PH = forms.IntegerField(label="Soil PH Content",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your soil nitrogen content'
        }))
    rainfall = forms.IntegerField(label="Rainfall",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter rainfall in mm'
        }))


class FertilizerPredictionForm(forms.Form):
    nitrogen = forms.IntegerField(label="Soil Nitrogen (N) Content",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your soil nitrogen content'
        }))
    phosphorus = forms.IntegerField(label="Soil Phosphorus (P) Content",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your soil phosphorus content'
        }))
    potassium = forms.IntegerField(label="Soil Potassium (K) Content",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your soil potassium content'
        }))
    moisture = forms.IntegerField(label="Soil Moisture Content",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your soil moisture content'
        }))
    soil_type= forms.CharField(label='Soil Type', widget=forms.Select(choices=SOIL_TYPES, attrs={
        'class': 'form-control',
        'placeholder': 'Enter your soil type'
        }))
    crop= forms.CharField(label='Name of your Crop', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your crop name'
        }))

class UserInputForm(forms.Form):
    userinput = forms.CharField(label="User Input",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your query'
        }))

class CropProduceListForm(forms.Form):
    name = forms.CharField(label="Product Name",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your commodity name'
        }))
    price = forms.IntegerField(label="Price per Quintal (in rupees)",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your proposed price per quintal'
        }))
    quantity = forms.IntegerField(label="Available Quantity (in quintals)",widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the available produce quantity'
        }))