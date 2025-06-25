from django.contrib.auth.models import User
from django.db import models



STATUS_CHOICES = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
)


class BaseModel(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # set once at creation
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)
    
    class Meta:
        abstract = True