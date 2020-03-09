# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import *
from . functions import *

from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView, Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
from django.utils import timezone

class UserNew(APIView):
    def post(self, request, format=None):
        jsonData, userSerializer = getUserJsonAndSerializer(request)
        if request.method == "POST":
            errors = Users.object.basicValidations(jsonData)
            if(errors):
                errors = sendErrors(request, errors)
                return Response({"errors": errors})
            else:
                errors = Users.object.emailValidation(jsonData)
                if(errors):
                    errors = sendErrors(request, errors)
                    return Response({"errors": errors})

            if userSerializer.is_valid():
                user = userSerializer.save()
                print(userSerializer.data)
                return Response({"user": userSerializer.data})
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
        return redirect('/')


def getUserJsonAndSerializer(request):
    try:
        jsonData = JSONParser().parse(request)
        print(jsonData)
        serializer = UserSerializer(data = jsonData)
    except Exception as err:
        serializer = {"error": err}

    return jsonData, serializer