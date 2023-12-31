from django.shortcuts import render
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from knox.auth import AuthToken

from accounts.serializer import RegisterSerializer
# Create your views here.


@api_view(["POST"])
def login(req):
    serializer = AuthTokenSerializer(data=req.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data["user"]
    _,token = AuthToken.objects.create(user)

    return Response({
        "userinfo":{
            "id" : user.id ,
            "username" : user.username,
        },
        "token" : token
    }
    )




@api_view(["POST"])
def register(req):
    serializer = RegisterSerializer(data=req.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    _,token = AuthToken.objects.create(user)

    return Response(
        {
        "userinfo":{
            "id" : user.id ,
            "username" : user.username
        },
        "token" : token
    }
    )