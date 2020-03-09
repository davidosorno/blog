from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


# When the system needs to store the value, it needs the userId as Int and 
# when the system needs to return the relationship it needs the nestead component
# however I can not save with the nestead component, so I created two serializers for that
class GetPostSerializer(serializers.ModelSerializer):
    userPostsFK = UserSerializer()
    class Meta:
        model = Posts
        fields = "__all__"

class SavePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"


class GetCommentSerializer(serializers.ModelSerializer):
    userCommentFK = UserSerializer()
    postCommentsFK = GetPostSerializer()
    class Meta:
        model = Comments
        fields = "__all__"

class SaveCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"