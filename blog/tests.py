from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Category, Tag, Blog, News


class CategoryAPITests(APITestCase):
    def test_create_category(self):
        data = {'title': 'Test Category'}
        response = self.client.post('/api/categories/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_categories(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_category(self):
        category = Category.objects.create(title='Existing Category')
        response = self.client.get(f'/api/categories/{category.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_category(self):
        category = Category.objects.create(title='Existing Category')
        updated_data = {'title': 'Updated Category'}
        response = self.client.put(f'/api/categories/{category.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        category = Category.objects.create(title='Existing Category')
        response = self.client.delete(f'/api/categories/{category.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TagAPITests(APITestCase):
    def test_create_tag(self):
        data = {'title': 'Sample tag'}
        response = self.client.post('/api/tags/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_tag(self):
        response = self.client.get('/api/tags/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_tag(self):
        tag = Tag.objects.create(title='Sample tag')
        response = self.client.get(f'/api/tags/{tag.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_tag(self):
        tag = Tag.objects.create(title='Sample tag')
        updated_data = {'title': 'Updated Tag'}
        response = self.client.put(f'/api/tags/{tag.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_tag(self):
        tag = Tag.objects.create(title='Sample tag')
        response = self.client.delete(f'/api/tags/{tag.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BlogAPITests(APITestCase):

    def setUp(self) -> None:
        self.user=User.objects.create(username='Leo')
        self.category=Category.objects.create(title='Football')
        self.tag=Tag.objects.create(title='#sport')
        self.blog=Blog.objects.create(       
            user= self.user,
            category= self.category,
            title= 'New Post',
            content= 'Description for post',)
        self.blog.tag.add(self.tag)
        
    def test_create_blog(self):
      
        data={
            'user': self.user.id,
            'category': self.category.id,
            'tag': [self.tag.id],
            'title': 'New Post',
            'content': 'Description for post',

        }
        response=self.client.post('/api/blog/', data, format='json')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_blog(self):
        response=self.client.get('/api/blog/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_blog(self):
        response=self.client.get(f'/api/blog/{self.blog.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_blog(self):
        updated_data = {
            'user': self.user.id,
            'category': self.category.id,
            'tag': [self.tag.id],
            'title': 'Updated Post',
            'content': 'Updated description',
        }
        response = self.client.put(f'/api/blog/{self.blog.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_blog(self):
        response = self.client.delete(f'/api/blog/{self.blog.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class NewsAPITests(APITestCase):

    def setUp(self) -> None:
        self.user=User.objects.create(username='Leo')
        self.category=Category.objects.create(title='Football')
        self.tag=Tag.objects.create(title='#sport')
        self.news=News.objects.create(       
            user= self.user,
            category= self.category,
            title= 'New Post for news',
            content= 'Description for news',)
        self.news.tag.add(self.tag)
        
    def test_create_news(self):
      
        data={
            'user': self.user.id,
            'category': self.category.id,
            'tag': [self.tag.id],
            'title': 'New Post',
            'content': 'Description for post',

        }
        response=self.client.post('/api/news/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_news(self):
        response=self.client.get('/api/news/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_retrieve_news(self):
        response=self.client.get(f'/api/news/{self.news.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_news(self):
        updated_data = {
            'user': self.user.id,
            'category': self.category.id,
            'tag': [self.tag.id],
            'title': 'Updated News',
            'content': 'Updated description for news',
        }
        response = self.client.put(f'/api/news/{self.news.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_news(self):
        response = self.client.delete(f'/api/news/{self.news.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


