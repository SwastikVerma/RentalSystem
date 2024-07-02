from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Customer(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = "__all__"

class Rent_historySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = "__all__"
