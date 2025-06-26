from rest_framework import serializers
from .models import *

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'created_by', 'updated_by', 'created_at',]
    
class BlogListSerializer(serializers.ModelSerializer):
    category_detail = BlogCategorySerializer(source='category', read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug','description','featured_image','category_detail',]


class BlogSerializer(serializers.ModelSerializer):
    category_detail = BlogCategorySerializer(source='category', read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'created_by', 'updated_by', 'created_at',]


