from django.shortcuts import render
from rest_framework import status
from . models import User
# Create your views here.
from rest_framework.views import APIView
from rest_framework.views import Response
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth import get_user_model

User = get_user_model()

class Register(APIView):
    # permission_classes = (AllowAny,)
    def post(self,request):
        name = request.data.get('username')
        email = request.data.get('email')
        password=request.data.get('password')
        address= request.data.get('address')
        if name and email:
            emp=User.objects.create_user(username=name,email=email,password=password,empAddress=address)
            emp.is_staff = True
            emp.is_superuser = True
            emp.save()
            return Response('data created succesfully')
        else:
            return Response('no username or email')

class Emps(APIView):
    """this class based function is used to make the curd operations"""
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def get(self,request):
        id = request.GET.get('id')
        if id:
            emp = User.objects.filter(empID=id).first()
            return Response({"user_id" : emp.id,
                        "username" : emp.username,
                        "email": emp.email,})
        else:
            return Response('no id provided')

    def put(self,request):
        id = request.data.get('id')
        password = request.data.get('password')
        emp= User.objects.get(id=id)
        emp.password = password
        emp.save()

    def delete(self,request):
        id = request.data.get('id')
        if id:
            record=User.objects.filter(id=id).delete()
            return Response("data is deleted")
        else:
            return Response("data not exists")
#
#JWT_KEY = "jwtactive987"
class Login(APIView):

    # permission_classes = (AllowAny,)

    def post(self, request, format="json"):
        user = request.data.get('user')
        password = request.data.get('password')
        user = authenticate(request, username=user, password=password)
        print(user)
        if user:
            login(request,user)
            return Response({
                        "user_id" : user.id,
                        "username" : user.username,
                        "email": user.email,

                        },
                        status=status.HTTP_200_OK)
        else:
            return Response({"user_status":False}, status=status.HTTP_401_UNAUTHORIZED)