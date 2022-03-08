from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255,default="MyBlog!")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255,default='coding')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title+ " | " + str(self.author)
    
    def get_absolute_url(self):
        # return reverse("article-detail",args=(str(self.id)))
        return reverse('home')
