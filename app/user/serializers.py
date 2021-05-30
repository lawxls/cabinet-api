from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        max_length=128, 
        required=True,
        write_only=True,
        min_length=5,
        validators=[validate_password])
    password2 = serializers.CharField(max_length=128, required=True, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('full_name', 'phone_number', 'email', 'password1', 'password2')
        extra_kwargs = {
            'full_name': {'required': True},
            'phone_number': {'required': True},
        }


    def create(self, validated_data):
        password1 = validated_data.get('password1')
        password2 = validated_data.pop('password2', None)

        if password1 and password2 and password1 != password2:
            msg = ('Пароли не совпадают')
            raise serializers.ValidationError(msg, code='password_mismatch')

        user = get_user_model().objects.create_user(validated_data['email'], validated_data['password1'])
        user.full_name = validated_data['full_name']
        user.phone_number = validated_data['phone_number']
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['email'] = user.email
        return token
