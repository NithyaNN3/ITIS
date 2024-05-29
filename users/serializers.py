from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password, check_password

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length = 100)
    last_name = serializers.CharField(max_length = 100)
    username = serializers.CharField(max_length = 100, required = True, validators = [UniqueValidator(queryset = User.objects.all(), message = "Username already exists. Kindly choose a different username.")])
    email = serializers.EmailField(required = True, validators = [UniqueValidator(queryset = User.objects.all())])
    password = serializers.CharField(write_only = True, required = True, validators = [validate_password])

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email", "password"]
        extra_kwargs = {
            "username": {"required": True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(first_name = validated_data["first_name"], last_name = validated_data["last_name"], username = validated_data["username"], email = validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = User
        fields = ["username", "password"]

class PasswordSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required = True)
    new_pass = serializers.CharField(write_only = True, required = True)
    old_pass = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = User
        fields = ["username", "new_pass", "old_pass"]

    def update(self, instance, validated_data):
        user = User.objects.get(username = validated_data['username'])
        user.password = make_password(validated_data['new_pass'])
        user.save()
        return user
    
    def validate(self, data):
        user = User.objects.get(username = data.get('username'))
        if user == None:
            raise serializers.ValidationError("Username is invalid.")
        if not check_password(data.get('old_pass'), user.password):
            raise serializers.ValidationError("Current password is invalid.")
        if data.get('old_pass') == data.get('new_pass'):
            raise serializers.ValueError("New password cannot be same as current password.")
        return data