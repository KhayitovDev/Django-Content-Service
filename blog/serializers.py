from rest_framework import serializers
from .models import Category, Tag, Blog, News

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['title']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['title']

class BlogSerializer(serializers.ModelSerializer):
    category=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tag=serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model=Blog
        fields=['id', 'user', 'category', 'tag', 'title', 'content', 'created_at', 'updated_at']


class NewsSerializer(serializers.ModelSerializer):
    category=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tag=serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model=News
        fields=['id', 'user', 'category', 'tag', 'title', 'content', 'created_at', 'updated_at']
