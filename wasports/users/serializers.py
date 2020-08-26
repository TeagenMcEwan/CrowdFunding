from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)


    def create(self, validated_data):

        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.ser_password(validated_data['password'])
        user.save()
        return user

        # return CustomUser.objects.create(**validated_data)

