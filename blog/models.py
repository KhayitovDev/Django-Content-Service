from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title=models.CharField(max_length=120)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    title=models.CharField(max_length=120)

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tag=models.ManyToManyField(Tag) # a blog can have several tags at a time
    title=models.CharField(max_length=220)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class News(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tag=models.ManyToManyField(Tag) # a blog can have several tags at a time
    title=models.CharField(max_length=220)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

