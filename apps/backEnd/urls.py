from django.contrib import admin
from django.conf.urls import include, url

from rest_framework import routers
from . import views, userviews, postviews, commentviews

router = routers.DefaultRouter()

app_name = "The Blog"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),

    url(r'^user/new$', userviews.UserNew.as_view()),
    url(r'^user/login$', views.LoginView.as_view()),
    url(r'^user/logout$', views.LogOut.as_view()),
    
    url(r'^home/getPosts/(?P<userId>\d+)$', postviews.GetAllPost.as_view()),
    url(r'^post/new$', postviews.PostNew.as_view()),
    # url(r'^post/delete/(?P<postId>\d+)/(?P<userId>\d+)$', views.DeletePost.as_view()),
    # url(r'^post/delete$', views.DeletePost.as_view()),    
    url(r'^post/delete$', postviews.DeletePost.as_view()),    
    url(r'^post/spam$', postviews.ReportPostAsSpam.as_view()),

    url(r'^home/getComments/(?P<userId>\d+)/(?P<postId>\d+)$', commentviews.GetAllComments.as_view()),
    url(r'^comment/new$', commentviews.CommentNew.as_view()),
    url(r'^comment/delete$', commentviews.DeleteComment.as_view()),    
    url(r'^comment/spam$', commentviews.ReportCommentAsSpam.as_view()),
]