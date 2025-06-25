from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User
from core.utils import *
from ckeditor.fields import RichTextField


class BlogCategory(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Blog(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(help_text="Short summary for listing page")
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    content = RichTextField()
    published_date = models.DateTimeField(auto_now_add=True)
    fb_url = models.URLField(max_length=200, null=True, blank=True)
    twitter_url = models.URLField(max_length=200, null=True, blank=True)
    linkedin_url = models.URLField(max_length=200, null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
