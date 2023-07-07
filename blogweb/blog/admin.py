from django.contrib import admin
from blog.models import AddBlog
from blog.models import Category

# Register your models here.
admin.site.register(AddBlog)
admin.site.register(Category)