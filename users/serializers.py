from rest_framework import serializers, validators
from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(validators=[validators.UniqueValidator(
        queryset=User.objects.all(), message="username already taken.")])
    email = serializers.CharField(validators=[validators.UniqueValidator(
        queryset=User.objects.all(), message="email already registered.")])
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField(allow_null=True, default=None)
    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        verify_is_employee = validated_data.get("is_employee")
        if verify_is_employee is True:
            return User.objects.create_superuser(
                **validated_data,
                is_superuser=True
                )
        else:
            return User.objects.create_user(
                **validated_data,
                is_superuser=False)
    
    def update(self, instance: User, validated_data: dict):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name",
                                                 instance.first_name)
        instance.last_name = validated_data.get("last_name",
                                                instance.last_name)
        instance.birthdate = validated_data.get("birthdate",
                                                instance.birthdate)
        instance.set_password(validated_data["password"])
        
        instance.save()
        return instance
