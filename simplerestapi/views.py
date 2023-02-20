from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer, LoginSerializer, StudentSerializer
from .helpers import get_tokens_for_user
from django.contrib.auth import authenticate
from .models import Student
from rest_framework.permissions import IsAuthenticated

class SignupAPIView(APIView):
    #This api will handle signup
    def post(self,request):
            serializer = SignupSerializer(data = request.data)
            if serializer.is_valid():
                    """If the validation success, it will created a new user."""
                    serializer.save()
                    res = { 'status' : status.HTTP_201_CREATED }
                    return Response(res, status = status.HTTP_201_CREATED)
            res = { 'status' : status.HTTP_400_BAD_REQUEST, 'data' : serializer.errors }
            return Response(res, status = status.HTTP_400_BAD_REQUEST)


def hello(request):
    data = [{'name': 'Peter', 'email': 'peter@example.org'},
            {'name': 'Julia', 'email': 'julia@example.org'}]
    return JsonResponse(data, safe=False)

class LoginAPIView(APIView):
    """This api will handle login and generate access and refresh token for authenticate user."""
    def post(self,request):
            serializer = LoginSerializer(data = request.data)
            if serializer.is_valid():
                    username = serializer.validated_data["username"]
                    password = serializer.validated_data["password"]
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        res_data = get_tokens_for_user(User.objects.get(username=username))
                        response = {
                               "status": status.HTTP_200_OK,
                               "message": "success",
                               "data": res_data
                               }
                        return Response(response, status = status.HTTP_200_OK)
                    else :
                        response = {
                               "status": status.HTTP_401_UNAUTHORIZED,
                               "message": "Invalid Email or Password",
                               }
                        return Response(response, status = status.HTTP_401_UNAUTHORIZED)
            response = {
                 "status": status.HTTP_400_BAD_REQUEST,
                 "message": "bad request",
                 "data": serializer.errors
                 }
            return Response(response, status = status.HTTP_400_BAD_REQUEST)


class StudentAPIView(APIView):
    #This api will handle student"""
    permission_classes = [IsAuthenticated]
    def get(self,request):
            data = Student.objects.all()
            serializer = StudentSerializer(data, many = True)
            response = {
                   "status": status.HTTP_200_OK,
                   "message": "success",
                   "data": serializer.data
                   }
            return Response(response, status = status.HTTP_200_OK)    