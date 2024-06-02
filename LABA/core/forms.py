from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from core.models import User
from django.core.exceptions import ValidationError
import re
from datetime import date
from toys.models import Rewiews
from django.utils import timezone
from toys.models import Vacancy


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username', 
        'class' : 'w-full py-4 px-6 rounded-xl'
        }))
    
    password=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your password',   
        'class' : 'w-full py-4 px-6 rounded-xl'
        }))
    



class SignupForm(UserCreationForm):
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your address',   
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your phone number (+375 (29) XXX-XX-XX)',   
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    date_of_birth = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Date of Birth'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'address', 'number', 'date_of_birth']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    def clean_number(self):
        number = self.cleaned_data.get('number')
        pattern = re.compile(r'^\+375 \(29\) \d{3}-\d{2}-\d{2}$')
        if not pattern.match(number):
            raise ValidationError('Phone number must be in the format +375 (29) XXX-XX-XX')
        return number
    
    
    def clean(self):
        cleaned_data = super().clean()
        date_of_birth = cleaned_data.get('date_of_birth')
        
        if date_of_birth:
            today = date.today()
            age = today.year - date_of_birth.year
            if today.month < date_of_birth.month or (today.month == date_of_birth.month and today.day < date_of_birth.day):
                age -= 1
            if age < 18:
                raise ValidationError('You must be at least 18 years old to register.')
        
        return cleaned_data
    
    
class RewiewsForm(forms.ModelForm):
    class Meta:
            model = Rewiews
            fields = ['rewiew', 'stars']
            widgets = {
                'rewiew': forms.Textarea(attrs={
                    'placeholder': 'Your review',
                    'class': 'w-full py-4 px-6 rounded-xl'
                }),
                'stars': forms.NumberInput(attrs={
                    'min': 1,
                    'max': 5,
                    'class': 'w-full py-4 px-6 rounded-xl'
                }),
            }

    def clean_stars(self):
        stars = self.cleaned_data.get('stars')
        if not (1 <= stars <= 5):
            raise forms.ValidationError('Rating must be between 1 and 5 stars.')
        return stars

    def save(self, commit=True):
        review = super().save(commit=False)
        review.date = timezone.now()  # Set the current date and time on the server
        if commit:
            review.save()
        return review
    
    
    
    
class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['proffesion', 'description']
        
        