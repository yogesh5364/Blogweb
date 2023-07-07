from django.shortcuts import render, redirect
from django.views import View
from .models import AddBlog
from users.models import AddUser

choices = ("Automobiles", "Automobiles"), ("Travel", "Travel"), ("Food", "Food"), ("Entertainment", "Entertainment"), (
"Covid", "Covid"), ()


# Create your views here.
def addblog(request):
    return render(request, "addblog.html")


class BlogAdd(View):
    def get(self, request):
        return redirect('/blog/addblog/')

    def post(self, request):
        title = request.POST.get("title")
        post = request.POST.get("post")
        email = request.session.get("email")
        obj = AddUser.objects.get(email=email)
        category = request.POST.get("category")
        AddBlog.objects.create(title=title, post=post, category=choices, author=obj)
        msg = "Successfully added the blog"
        return render(request, "addblog.html", {'msg': msg})


class BlogCat(View):
    def get(self, request):
        return redirect('/blog/addblog/')


def showblog(request):
    blog = AddBlog.objects.all()
    return render(request, "showblog.html", {'blog': blog})
