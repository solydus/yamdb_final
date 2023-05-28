from rest_framework import serializers
from .models import User
import re

ADMIN_ROLE = 'admin'


class RegisterDataSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(regex=r'^[\w.@+-]+$',
                                      max_length=150,
                                      required=True)
    email = serializers.EmailField(max_length=254)

    def validate_username(self, value):
        if len(value) > 150:
            raise serializers.ValidationError('Not mach len')
        pattern_username = '[A-Za-z0-9+-_@]+'
        if re.match(pattern_username, value) is None:
            raise serializers.ValidationError('Incorrect symbol')
        return value

    class Meta:
        fields = ('username', 'email')
        model = User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email'
        )

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')

        if username == 'me':
            raise serializers.ValidationError('нельзя использовать')

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('попробуйте ещё раз')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('попробуйте ещё раз')

        return data


class UserRecieveTokenSerializer(serializers.Serializer):

    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=150,
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=150,
        required=True
    )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('попробуйте ещё раз')
        return value

    def validate_role(self, value):
        if not self.instance:
            return value
        if self.instance.role != ADMIN_ROLE:
            return self.instance.role
        return value
