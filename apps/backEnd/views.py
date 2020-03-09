# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from . models import *
from . functions import *
from . userviews import UserSerializer

from rest_framework.views import APIView, Response

class LoginView(APIView):
    def post(self, request, format = None):
        user = Users.objects.filter(superUser = True)
        if not user:
            print("Creand")
            user = Users()
            user.firstName = "Super User Root"
            user.email = "root@root.com"
            user.superUser = True
            user.save()

        data = Login(self, request)
        if data == None:
            errors = {}
            errors["login"] = "We can't find the email. Please register."
            return Response({"errors": errors})
        
        return Response(data)


class LogOut(APIView):
    def get(self, request):
        return redirect('/')


def Login(self, request):
    email = request.data["email"]
    if email == "":
        errors = {}
        errors["login"] = "Email is required."
        return {"errors": errors}
    user = Users.objects.filter(email = email)
    if user:
        user = user[0]
        userSerializer = UserSerializer(user)
        print(userSerializer.data)
        return {"user": userSerializer.data}

    return None