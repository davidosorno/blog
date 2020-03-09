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


class PostNew(APIView):
    def post(self, request, format = None):
        jsonData = JSONParser().parse(request)
        # print(jsonData)
        serializer = SavePostSerializer(data = jsonData)
        # print(serializer)
        if request.method == "POST":
            errors = Posts.object.messageValidation(jsonData["message"], "Post")
            if(errors):
                errors = sendErrors(request, errors)
                return Response({"errors": errors})
                
            print("Json: ", jsonData)
            print("Serializer: ", serializer)
            try:
                if serializer.is_valid():
                    post = serializer.save()
                    serializer = SavePostSerializer(post)
                    print("Serializer Data: ", serializer.data)
                    return Response({"post": serializer.data})
                else:
                    print("Error: struct not valid.", serializer.errors)
                    return Response(status.HTTP_400_BAD_REQUEST)
            except Exception as err:
                print("Error: struct not valid.", err)
            
        return redirect('/')


class GetAllPost(APIView):
    def get(self, request, userId):
        user = Users.objects.filter(id = userId, superUser = True)
        print(user)
        if user:
            posts = Posts.objects.all().order_by("-id")
        else:
            posts = Posts.objects.filter(spam = False).order_by("-id")
        postSerializer = GetPostSerializer(posts, many = True)
        # print(postSerializer.data)
        return Response({"posts": postSerializer.data})


class DeletePost(APIView):
    # We can delete utilizing the rout delete/post/IdPost, however we have to check for the super user and it's easyiest with post method
    # def delete(self, request, postId, userId):
    #     errors = {}
    #     try:
    #         post = Posts.objects.get(id = postId, userPostsFK = userId)
    #         if post:
    #             post.delete()
    #             return Response(True)
    #     except:
    #         errors = sendErrors(request, errors)
    #         return Response({"errors": errors})

    def post(self, request):
        errors = {}
        jsonData = JSONParser().parse(request)
        if request.method == "POST":
            print(jsonData["user"]["firstName"])
            try:
                if not jsonData["user"]["superUser"]:
                    post = Posts.objects.get(
                        id = jsonData["postId"], 
                        userPostsFK = jsonData["user"]["id"]
                        )
                else:
                    post = Posts.objects.get(id = jsonData["postId"])

                if post:
                    post.delete()
                    return Response(True)

            except:
                errors = sendErrors(request, errors)
                return Response({"errors": errors})



class ReportPostAsSpam(APIView):
    def put(self, request):
        errors = {}
        try:
            post = Posts.objects.get(id = request.data["postId"])
            if post:
                post.spam = True
                post.save()
                return Response(True)
        except Exception as err:
            return Response({"errors": str(err)})