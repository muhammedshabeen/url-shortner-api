from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User
from core.utils import *
from ckeditor_uploader.fields import RichTextUploadingField

class BlogCategory(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1

            while self.__class__.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{num}"
                num += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Blog(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(help_text="Short summary for listing page")
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    content = RichTextUploadingField()
    published_date = models.DateTimeField(auto_now_add=True)
    fb_url = models.URLField(max_length=200, null=True, blank=True)
    twitter_url = models.URLField(max_length=200, null=True, blank=True)
    linkedin_url = models.URLField(max_length=200, null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1

            while self.__class__.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{num}"
                num += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# class Plan(BaseModel):
#     PLAN_TYPES = (
#         ('FREE', 'Free'),
#         ('PRO', 'Pro'),
#         ('BULK', 'Bulk 100K'),
#         ('ENTERPRISE', 'Enterprise'),
#     )
#     name = models.CharField(max_length=100, choices=PLAN_TYPES, unique=True)
#     price_per_month = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     price_per_year = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     custom_pricing = models.BooleanField(default=False)
#     monthly_url_limit = models.PositiveIntegerField(null=True, blank=True)
#     monthly_click_limit = models.PositiveIntegerField(null=True, blank=True)
#     description = models.TextField(null=True, blank=True)  # e.g., "500 Links with Unlimited Trackable Clicks"
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.get_name_display()
    


# class FeatureCategory(BaseModel):
#     name = models.CharField(max_length=100) 

#     def __str__(self):
#         return self.name
    

# class Feature(BaseModel):
#     name = models.CharField(max_length=100)
#     description = models.TextField(null=True, blank=True)
#     category = models.ForeignKey(FeatureCategory, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


# class PlanFeature(BaseModel):
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='plan_features')
#     feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='feature_plans')
#     is_available = models.BooleanField(default=False)
#     limit_info = models.CharField(max_length=100, null=True, blank=True)

#     class Meta:
#         unique_together = ('plan', 'feature')

#     def __str__(self):
#         return f"{self.plan.name} - {self.feature.name}"


