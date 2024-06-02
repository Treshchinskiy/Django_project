from django import forms
from .models import Product, ProductType
from django.core.exceptions import ValidationError

INPUT_CLASSES='2-full py-4 px-6 rounded-xl border'



class ProductForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('not available', 'Not Available')
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES)
    product_type_id = forms.ModelChoiceField(queryset=ProductType.objects.all())

    class Meta:
        model = Product
        fields = ['name', 'product_code', 'price', 'image', 'status', 'product_type_id', 'amount']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Product Name',
                'class': 'w-full py-2 px-3 rounded'
            }),
            'product_code': forms.TextInput(attrs={
                'placeholder': 'Product Code',
                'class': 'w-full py-2 px-3 rounded'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Price',
                'class': 'w-full py-2 px-3 rounded'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-2 px-3 rounded'
            }),
            'amount': forms.NumberInput(attrs={
                'placeholder': 'Amount',
                'class': 'w-full py-2 px-3 rounded'
            }),
        }



class ToyOrderForm(forms.Form):
    toy = forms.ModelChoiceField(queryset=Product.objects.all(), label='Select Toy')
    number_of_toys = forms.IntegerField(label='Number of Toys', min_value=1)
    promocode = forms.CharField(label='Promo Code', required=False)
    
    """  def clean(self):
        cleaned_data = super().clean()
        toy = cleaned_data.get('toy')
        number_of_toys = cleaned_data.get('number_of_toys')

        if toy and number_of_toys:
            if toy.amount < number_of_toys:
                raise ValidationError( 
                    f'There are only {toy.amount} units of {toy.name} available.'
                )
        return cleaned_data """