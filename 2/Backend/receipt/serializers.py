from rest_framework import serializers
from . models import TollReceipt

class TollReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = TollReceipt
        fields = "__all__"