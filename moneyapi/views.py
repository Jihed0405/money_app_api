from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Money
from .serializers import MoneySerializer


class MoneyApiView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

  def get(self, request, id=None):
    if id:
      # If an id is provided in the GET request, retrieve the Money transaction by that id
      try:
        # Check if the Money transaction the user wants to update exists
        queryset = Money.objects.get(id=id)
      except Money.DoesNotExist:
        # If the Money transaction does not exist, return an error response
        return Response({'errors': 'This Money transaction does not exist.'}, status=400)

      # Serialize Money Transaction from Django queryset object to JSON formatted data
      read_serializer = MoneySerializer(queryset)

    else:
      # Get all Money Transactions from the database using Django's model ORM
      queryset = Money.objects.all()

      # Serialize list of Money Transactions from Django queryset object to JSON formatted data
      read_serializer = MoneySerializer(queryset, many=True)

    # Return a HTTP response object with the list of Money Transactions as JSON
    return Response(read_serializer.data)


  def post(self, request):
    # Pass JSON data from user POST request to serializer for validation
    create_serializer = MoneySerializer(data=request.data)

    # Check if user POST data passes validation checks from serializer
    if create_serializer.is_valid():

      # If user data is valid, create a new Money transaction record in the database
      money_transaction_object = create_serializer.save()

      # Serialize the new Money transaction from a Python object to JSON format
      read_serializer = MoneySerializer(money_transaction_object)

      # Return a HTTP response with the newly created Money transaction data
      return Response(read_serializer.data, status=201)

    # If the users POST data is not valid, return a 400 response with an error message
    return Response(create_serializer.errors, status=400)


  def put(self, request, id=None):
    try:
      # Check if the Money transaction the user wants to update exists
      money_transaction = Money.objects.get(id=id)
    except Money.DoesNotExist:
      # If the Money transaction does not exist, return an error response
      return Response({'errors': 'This Money Transaction does not exist.'}, status=400)

    # If the Money transaction does exists, use the serializer to validate the updated data
    update_serializer = MoneySerializer(money_transaction, data=request.data)

    # If the data to update the Money transaction is valid, proceed to saving data to the database
    if update_serializer.is_valid():

      # Data was valid, update the Money transaction in the database
      money_transaction_object = update_serializer.save()

      # Serialize the Money transaction from Python object to JSON format
      read_serializer = MoneySerializer(money_transaction_object)

      # Return a HTTP response with the newly updated Money transaction
      return Response(read_serializer.data, status=200)

    # If the update data is not valid, return an error response
    return Response(update_serializer.errors, status=400)


  def delete(self, request, id=None):
    try:
      # Check if the Money transaction the user wants to update exists
      money_transaction = Money.objects.get(id=id)
    except Money.DoesNotExist:
      # If the Money transaction does not exist, return an error response
      return Response({'errors': 'This Money Transaction does not exist.'}, status=400)

    # Delete the chosen Money transaction from the database
    money_transaction.delete()

    # Return a HTTP response notifying that the Money transaction was successfully deleted
    return Response(status=204)