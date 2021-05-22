import coreschema
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from . models import TollReceipt
from .serializers import TollReceiptSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import coreapi
from rest_framework.schemas import AutoSchema
from datetime import date, datetime

class ReceiptViewSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field(name='vehicle_number', required=True, description="Vehicle Registration Number"),
                coreapi.Field(name='journey_type', required=True, description="Single or Return Journey"),
                coreapi.Field(name='vehicle_type', required=True, description="Car or Bus or Truck"),
                coreapi.Field(name='journey_status', required=True, description="Journey Started or Ended"),
                coreapi.Field(name='journey_towards', required=True, description="Source to Destination"),
                coreapi.Field(name='price', required=True, description="Toll ticket price", schema=coreschema.Integer())
            ]
        manual_fields = super(ReceiptViewSchema, self).get_manual_fields(path, method)
        return manual_fields + extra_fields

class Receipt(APIView):

    schema = ReceiptViewSchema()

    def get(self, request):
        receipts = TollReceipt.objects.all()
        serializer = TollReceiptSerializer(receipts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TollReceiptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReceiptDetails(APIView):

    schema = ReceiptViewSchema()

    def get_object(self, id):
        try:
            return TollReceipt.objects.get(receipt_id=int(id))
        except TollReceipt.DoesNotExist:
            return "Record doesn't exists"

    def get(self, request, id):
        today = datetime.now()
        receipt = self.get_object(id)
        if isinstance(receipt,str) and receipt == "Record doesn't exists":
            return Response({"message": "No Receipt exists with the ID " + str(id)}, status=status.HTTP_404_NOT_FOUND)
        serializer = TollReceiptSerializer(receipt)

        if receipt.get_price() == 100:
            return Response({"message": "Not a valid return Ticket", "data": serializer.data}
                            , status=status.HTTP_406_NOT_ACCEPTABLE)
        elif today.date() != receipt.get_journey_date_time().date():
            return Response({"message": "The Ticket has been expired!. Please, take a new one", "data": serializer.data}
                            , status=status.HTTP_406_NOT_ACCEPTABLE)
        elif receipt.get_journey_status() == 'end':
            return Response({"message": "Service Availed!!!, Please, take a new one", "data": serializer.data}
                            , status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(serializer.data)

    def put(self, request, id):
        receipt = self.get_object(id)
        serializer = TollReceiptSerializer(receipt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        receipt = self.get_object(id)
        receipt.delete()
        return Response({"message": "Receipt with the ID " + str(id) + " deleted."}, status=status.HTTP_204_NO_CONTENT)