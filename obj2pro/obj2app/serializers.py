from rest_framework import serializers
from dataclasses import field, fields

from .models import *


class DetectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Detect
        fields = '__all__'