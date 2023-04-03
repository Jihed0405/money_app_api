from rest_framework import serializers

from .models import Money


class MoneySerializer(serializers.ModelSerializer):
   
    categoryType = serializers.CharField(max_length=1000)
    type = serializers.CharField(max_length=1)
    itemCategoryName = serializers.CharField(
    max_length=1000,
    )
    itemName = serializers.CharField(
    max_length=1000,
    )

    amount = serializers.DecimalField(
    max_digits=10, decimal_places=3  
    )
  
  
    date = serializers.DateTimeField(
    
    )
    def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        return Money.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
        instance.categoryType = validated_data.get('categoryType', instance.categoryType)
        instance.type = validated_data.get('type', instance.type)
        instance.itemCategoryName = validated_data.get('itemCategoryName', instance.itemCategoryName)
        instance.itemName = validated_data.get('itemName', instance.itemName)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

