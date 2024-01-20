from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Category, Tag, Blog, News
from .serializers import CategorySerializer, TagSerializer, BlogSerializer, NewsSerializer

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            headers=self.get_success_headers(serializer.data)
            return Response({'message': 'Category has been created successfully'}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({'message': 'Category has been updated successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance=self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Category has been deleted successfully'})
    
class TagViewSet(ModelViewSet):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            headers=self.get_success_headers(serializer.data)
            return Response({'message': 'Tag has been created successfully'}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({'message': 'Tag has been updated successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance=self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Tag has been deleted successfully'})
    
class BlogViewSet(ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            headers=self.get_success_headers(serializer.data)
            return Response({'message': 'Blog has been created successfully'}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({'message': 'Blog has been updated successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance=self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Blog has been deleted successfully'})
    
class NewsViewSet(ModelViewSet):
    queryset=News.objects.all()
    serializer_class=NewsSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            headers=self.get_success_headers(serializer.data)
            return Response({'message': 'News has been created successfully'}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({'message': 'News has been updated successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance=self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'News has been deleted successfully'})
    

    
