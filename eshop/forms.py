from django import forms


class ProductFormWidget(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название продукта'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.FloatField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    qty = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    img = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
