from rest_framework import serializers
from .models import Datalist

class DatalistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Datalist
        fields=("id", "name", "city","cardnumber","phonenumber","created","token")
