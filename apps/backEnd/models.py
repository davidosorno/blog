# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date, datetime
import re #It allows us to create string validation that we can use to verify the email

#Here we have all valid character to create an email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class BasicValidators(models.Model):

    def basicValidations(self, postData):
        print(postData)
        errors = {}
        if(len(postData["firstName"]) < 3):
            errors["firstName"] = "The first name must be greater than 3 characters."
        
        if(len(postData["firstName"]) > 25):
            errors["firstName"] = "The first name can not be greater than 25 characters."
        
        return errors

    def emailValidation(self, postData):
        errors = {}
        if postData["email"] == "":
            errors["email"] = "Email is required."
        else:
            # Check email syntax
            if not EMAIL_REGEX.match(postData["email"].strip()):
                errors["email"] = "The email is not valid."
            else:
                # Check if the email is already in the database
                user = Users.objects.filter(email = postData['email'].strip())
                if user:
                    errors["email"] = "Email is already in the database."

        return errors

    def messageValidation(self, message, title):
        errors = {}
        if(len(message) < 3):
            errors[title] = "The message must be greater than 3 characters."
        
        if(len(message) > 255):
            errors[title] = "The message can not be greater than 255 characters."

        return errors


class Users(models.Model):
    #id
    firstName = models.CharField(max_length = 25)
    email = models.CharField(max_length = 50)
    superUser = models.BooleanField(default=False)
    
    object = BasicValidators()
    
    
class Posts(models.Model):
    #id
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    spam = models.BooleanField(default=False)

    userPostsFK = models.ForeignKey(Users, related_name="postUserFK", on_delete=models.PROTECT)
    object = BasicValidators()


class Comments(models.Model):
    #id
    comment = models.TextField()
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    spam = models.BooleanField(default=False)

    postCommentsFK = models.ForeignKey(Posts, related_name="commentsPostFK", on_delete=models.PROTECT)
    userCommentFK = models.ForeignKey(Users, related_name='commentsUserFK', on_delete=models.PROTECT)
    object = BasicValidators()


class NumUsersConnected(models.Model):
    #id
    numUsers = models.IntegerField(default=0)