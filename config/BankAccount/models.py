from django.db import models

# Create your models here.
class BankAccount(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    account_holder = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.account_holder} - {self.account_number}"
    
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    )
    bank_account = models.ForeignKey(BankAccount, related_name='transactions', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} of {self.amount} on {self.timestamp}"
# we need to import the User model from django.contrib.auth.models
