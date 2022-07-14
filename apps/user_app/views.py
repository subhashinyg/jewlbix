from typing_extensions import Self
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .serializers import *
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
usermodel= get_user_model()
from rest_framework.exceptions import ValidationError, ParseError
from rest_framework.views import APIView


class UserManageView(APIView):
    
    def post(self, request, *args, **kwargs):

        if usermodel.objects.filter(mobile_no= request.data['mobile_no']):
            return Response({"error occured": "User already exist"})

        serializer= UserCreateSerializer(data= request.data)

        serializer. is_valid(raise_exception= True)
        user= serializer.save()
        token, created= Token.objects.get_or_create(user= user)
        return Response({"message":"User Created Successfuly","token":token.key})
        
class UserLoginView(APIView):
    def post(self,request, *args, **kwargs):
        try:
            qr= usermodel.objects.filter(mobile_no= request.data['mobile_num'])[0]
            if qr:
                
                token,_=Token.objects.get_or_create(user= qr.id)
                return Response({'key':token.key})
            return Response({"Error":"User not exist"})
        except:
            return Response({"Error":"Error occure may be unknown user"})
            

        
def welcome(request):
    return HttpResponse("welcome")
        

       
    