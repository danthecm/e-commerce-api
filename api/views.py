from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AdminSerializer
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import generics
# Create your views here.


class CreateAdmin(generics.CreateAPIView):
    """
    creates an admin user

    """
    queryset = User.objects.all()
    serializer_class = AdminSerializer
