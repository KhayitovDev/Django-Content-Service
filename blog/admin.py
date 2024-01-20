from django.contrib import admin
from .models import Category, Tag, Blog, News


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(News)
