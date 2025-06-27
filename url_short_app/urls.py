from django.urls import path
from .views import *

urlpatterns = [

    #Authentication
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),

    #BlogCategory
    path('blog-categories/', BlogCategoryAPIView.as_view(), name='blog-category'),
    path('blog-categories/<int:pk>/', BlogCategoryAPIView.as_view(), name='blog-category'),

    #Blog
    path('blogs/', BlogListCreateAPIView.as_view(), name='blog'),
    path('blogs/<int:pk>/', BlogDetailAPIView.as_view(), name='blog-detail'),
    
    #Plan
    path("plans/", PlansAPIView.as_view(), name="plans"),
]
