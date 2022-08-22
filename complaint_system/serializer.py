from rest_framework import serializers

from .models import *

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['full_name', 'email', 'password', 'role']