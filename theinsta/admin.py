from cProfile import Profile
from django.contrib import admin
from . models import Post, Profile, Comment, Category
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)