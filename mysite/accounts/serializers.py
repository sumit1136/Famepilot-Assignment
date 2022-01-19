from accounts.models import Person
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('username','first_name','last_name','email','DOB','phone')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=100,
        style={'placeholder': 'username', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
            else:
                data['user'] = user
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')
        return data

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=100,
        style={'placeholder': 'username', 'autofocus': True}
    )
    fname = serializers.CharField(
        max_length=100,
        label='First Name',
        style={'placeholder': 'First Name'}
    )
    lname = serializers.CharField(
        max_length=100,
        label='Last Name',
        style={'placeholder': 'Last Name'}
    )
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email'}
    )
    mobile = serializers.CharField(
        max_length=100,
        style={'placeholder': 'XXXXXXXXXX','input_type':'tel'}
    )
    DOB = serializers.DateField(
        label='Date of Birth',
        style = {'input_type':'date'}
    )
    passw = serializers.CharField(
        label='Password',
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    def validate(self, data):
        username = data.get('username')
        fname = data.get('fname')
        lname = data.get('lname')
        email = data.get('email')
        phone = data.get('mobile')
        DOB = data.get('DOB')
        passw = data.get('passw')
        x = Person.objects.create(username = username, first_name = fname, last_name = lname, email=email, phone=phone,DOB=DOB)
        data['person'] = x
        y = User.objects.create_user(username=username,password = passw)
        data['user'] = y
        return data
    

