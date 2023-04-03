from django.db import models
  
 


# Create your models here.
class Money(models.Model):
    TRANSACTION_TYPE_INFLOW = 'I'
    TRANSACTION_TYPE_OUTFLOW = 'O'
    
    TRANSACTION_TYPE = [
    (TRANSACTION_TYPE_INFLOW, 'Income'),
    (TRANSACTION_TYPE_OUTFLOW, 'Expenses'),
    
    ]
    categoryType = models.CharField(
    max_length=1000,
    )
    type = models.CharField(max_length=1, choices=TRANSACTION_TYPE, default=TRANSACTION_TYPE_OUTFLOW)
    itemCategoryName = models.CharField(
    max_length=1000,
    )
    itemName = models.CharField(
    max_length=1000,
    )

    amount = models.DecimalField(
    max_digits=10, decimal_places=3  
    )
  
  
    date = models.DateTimeField(
    
    )



    