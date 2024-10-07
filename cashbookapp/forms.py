from django import forms
from .models import cash_entry
from django.contrib.auth.forms import AuthenticationForm
class cash_entry_form(forms.ModelForm):
    class Meta:
        model = cash_entry
        fields = ['name', 'amount', 'cash_type', 'tran_type', 'tran_plat']
        labels = {
            'name': 'Name', 
            'amount': 'Amount',
            'cash_type': 'Cash In/Out', 
            'tran_type': 'Transaction Type', 
            'tran_plat': 'Transaction Platform',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg rounded-pill', 
                'placeholder': 'Enter Name'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control form-control-lg rounded-pill', 
                'placeholder': 'Enter Amount'
            }),
            'cash_type': forms.Select(attrs={
                'class': 'form-select form-select-lg rounded-pill',
            }),
            'tran_type': forms.Select(attrs={
                'class': 'form-select form-select-lg rounded-pill',
            }),
            'tran_plat': forms.Select(attrs={
                'class': 'form-select form-select-lg rounded-pill',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding a disabled option as a placeholder while preserving all the original choices
        self.fields['cash_type'].choices = [('', 'Select Cash Type')] + list(self.fields['cash_type'].choices)
        self.fields['tran_type'].choices = [('', 'Select Transaction Type')] + list(self.fields['tran_type'].choices)
        self.fields['tran_plat'].choices = [('', 'Select Transaction Platform')] + list(self.fields['tran_plat'].choices)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))