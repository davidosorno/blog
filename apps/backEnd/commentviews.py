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


class CommentNew(APIView):
    def post(self, request, format = None):
        jsonData = JSONParser().parse(request)
        # print(jsonData)
        serializer = SaveCommentSerializer(data = jsonData)
        # print(serializer)
        if request.method == "POST":
            errors = Comments.object.messageValidation(jsonData["comment"], "Comment")
            if(errors):
                errors = sendErrors(request, errors)
                return Response({"errors": errors})
                
            print("Json: ", jsonData)
            print("Serializer: ", serializer)
            try:
                if serializer.is_valid():
                    comment = serializer.save()
                    serializer = SaveCommentSerializer(comment)
                    print("Serializer Data: ", serializer.data)
                    return Response({"comment": serializer.data})
                else:
                    print("Error: struct not valid.", serializer.errors)
                    return Response(status.HTTP_400_BAD_REQUEST)
            except Exception as err:
                print("Error: struct not valid.", err)
            
        return redirect('/')


class GetAllComments(APIView):
    def get(self, request, userId, postId):
        user = Users.objects.filter(id = userId, superUser = True)
        print(user)
        if user:
            comments = Comments.objects.filter( 
                postCommentsFK = postId
            ).order_by("-id")
        else:
            comments = Comments.objects.filter(
                spam = False, 
                postCommentsFK = postId
            ).order_by("-id")

        commentSerializer = GetCommentSerializer(comments, many = True)
        print(commentSerializer.data)
        return Response({"comments": commentSerializer.data})


class DeleteComment(APIView):
    def post(self, request):
        errors = {}
        jsonData = JSONParser().parse(request)
        if request.method == "POST":
            # print(jsonData["user"]["firstName"])
            try:
                if not jsonData["user"]["superUser"]:
                    # print(jsonData["idPost"])
                    # print(jsonData["idComment"])
                    # print(jsonData["user"]["id"])
                    comment = Comments.objects.get(
                        id = jsonData["idComment"], 
                        userCommentFK = jsonData["user"]["id"],
                        postCommentsFK = jsonData["idPost"]
                    )
                else:
                    comment = Comments.objects.get(id = jsonData["idComment"])

                if comment:
                    print(1)
                    comment.delete()
                    return Response(True)

            except Exception as err:
                print(err)
                errors = sendErrors(request, errors)
                return Response({"errors": errors})


class ReportCommentAsSpam(APIView):
    def put(self, request):
        errors = {}
        try:
            comment = Comments.objects.get(id = request.data["idComment"])
            if comment:
                comment.spam = True
                comment.save()
                return Response(True)
        except Exception as err:
            return Response({"errors": str(err)})