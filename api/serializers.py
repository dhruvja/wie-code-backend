from rest_framework import serializers
from .models import Document, Track, UserInfo, EmergencyContacts, Qr
from django.contrib.auth.models import User

class DocumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','email','password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )
        return user

class UserSerializer(serializers.ModelSerializer):

    class Meta: 
        model = User
        fields = ('id', 'username', 'email')

class TrackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Track
        fields = '__all__'

class QrSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qr
        fields = '__all__'

class EmergencyContactsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmergencyContacts 
        fields = '__all__'

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = "__all__"