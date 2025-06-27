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


class BillingCycle(models.TextChoices):
    MONTHLY = 'monthly', 'Monthly'
    ANNUAL = 'annual', 'Annual'
    
class LinkVolume(models.Model):
    label = models.CharField(max_length=20)
    link_count = models.BigIntegerField(null=True, blank=True)

    
    def __str__(self):
        return self.label
    
class Feature(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=100)
    display_order = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

class PlanPricing(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    link_volume = models.ForeignKey(LinkVolume, on_delete=models.CASCADE,null=True,blank=True)
    billing_cycle = models.CharField(max_length=10, choices=BillingCycle.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    annual_equivalent_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True,blank=True)

    class Meta:
        unique_together = ('plan', 'link_volume', 'billing_cycle')

    def __str__(self):
        return f"{self.plan.name} ({self.link_volume.label if self.link_volume else 'free'}, {self.billing_cycle})"
    
class PlanFeatureValue(models.Model):
    plan_pricing = models.ForeignKey(PlanPricing, on_delete=models.CASCADE, related_name='feature_values')
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.plan_pricing} - {self.feature.name}: {self.value}"

