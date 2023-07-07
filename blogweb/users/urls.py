from django.urls import path 
from django.urls.conf import  path, include
from . import views 

urlpatterns = [
    path('', views.index),
    path("blog_login/", views.login),
    path("blog_signup/", views.signup),
    path("aftersignup/", views.aftersignup),
    path("afterlogin/", views.afterlogin.as_view()),
    path("logout/", views.logout),
    path("forgot/", views.forgot),
    path("getemail/", views.Getemail.as_view()),
    path("checkotp/", views.Checkotp.as_view()),
    path("changepass/", views.Changepass.as_view()),
    path("blog_about/", views.about),
    path("blog/", include("blog.urls"))   
]