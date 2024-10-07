from django.db import models

class cash_entry(models.Model):
    name = models.CharField(max_length=256)
    amount = models.IntegerField()

    cash_choices = [
        ('cash_in', 'Cash In'),
        ('cash_out', 'Cash Out')
    ]
    
    transaction_type_choices = [
        ('upi', 'UPI'),
        ('cash', 'Cash')
    ]
    
    transaction_platform_choices = [
        ('phonepe', 'PhonePe'),
        ('googlepay', 'Google Pay'),
        ('paytm', 'Paytm')
    ]
    
    cash_type = models.CharField(max_length=10, choices=cash_choices, default='NULL')
    tran_type = models.CharField(max_length=50, choices=transaction_type_choices, default='NULL')
    tran_plat = models.CharField(max_length=50, choices=transaction_platform_choices, null=True, blank=True)  # Allowing null and blank
    
    def __str__(self):
        return f"{self.name}"

    def clean(self):
        from django.core.exceptions import ValidationError
        # Ensure platform is selected for UPI transactions
        if self.tran_type == 'upi' and not self.tran_plat:
            raise ValidationError("Transaction platform must be selected for UPI transactions.")
        # Reset tran_plat if transaction is not UPI
        if self.tran_type != 'upi':
            self.tran_plat = None  # Clear tran_plat when not UPI
