from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Student

class SignupSerializer(serializers.ModelSerializer):
    #override create method to change the password into hash."""
    def create(self, validate_data):
            validate_data["password"] = make_password(validate_data.get("password"))
            return super(SignupSerializer, self).create(validate_data)
    class Meta:
            model = User
            fields = ['username','password']
            
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
            model = User
            fields = ['username','password']            
            
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
            model = Student
            fields = ['name','email','created_at','updated_at']
