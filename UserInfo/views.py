from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserInfo
from UserInfo.models import UserInfo
from UserInfo.serializer_user import UserInfoSerializer


class UsersList(APIView):

    def get(self,url):
        allusers=UserInfo.objects.all()
        serializer=UserInfoSerializer(allusers,many=True)
        return Response(serializer.data)

    def post(self):
        pass

