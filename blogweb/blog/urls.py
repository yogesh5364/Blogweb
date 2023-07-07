from django.urls.conf import path 
from . import views

urlpatterns = [
    path('addblog/', views.addblog),
    path("afteraddblog/", views.BlogAdd.as_view()),
    path("afteraddblog/", views.BlogCat.as_view()),
    path("showblog/", views.showblog)
]