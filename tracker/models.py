from django.db import models


class curr_balance(models.Model):
    balance = models.FloatField(default=0.0)
    def __str__(self):
        return str(self.balance)

# Create your models here.
class track_history(models.Model):
    balance = models.ForeignKey(curr_balance, on_delete = models.CASCADE)
    amount = models.FloatField()
    expense_type = models.CharField(choices = (('Credit', 'Credit'), ('Debit', 'Debit')), max_length=10)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

