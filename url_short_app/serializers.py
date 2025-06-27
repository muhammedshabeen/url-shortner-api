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
        
        


class FeatureValueSerializer(serializers.ModelSerializer):
    feature_name = serializers.CharField(source='feature.name')
    feature_category = serializers.CharField(source='feature.category')

    class Meta:
        model = PlanFeatureValue
        fields = ['feature_name', 'feature_category', 'value']


class PlanPricingSerializer(serializers.ModelSerializer):
    link_volume = serializers.SerializerMethodField()
    features = FeatureValueSerializer(source='feature_values', many=True)

    class Meta:
        model = PlanPricing
        fields = ['link_volume', 'billing_cycle', 'price', 'annual_equivalent_price', 'features']
    
    def get_link_volume(self, obj):
        if obj.link_volume:
            return obj.link_volume.label
        elif obj.plan.name == 'Enterprise':
            return 'Custom'
        elif obj.plan.name == 'Free':
            return "Free"
        else:
            return None



