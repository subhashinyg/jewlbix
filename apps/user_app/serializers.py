from rest_framework import serializers
from django.contrib.auth import get_user_model

usermodel= get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= usermodel
        fields= ['username', 'mobile_no','lat' ,'lon', 'user_type','status','district',
        'town','is_verified','fcm_token' ]

