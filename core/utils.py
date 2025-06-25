from django.contrib.auth.models import User
from django.db import models



STATUS_CHOICES = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
)


class BaseModel(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    soft_delete = models.BooleanField(default=False)
    
    class Meta:
        abstract = True