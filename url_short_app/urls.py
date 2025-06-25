from django.urls import path
from .views import *

urlpatterns = [

    #Authentication
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),

    #Blog
    path('blog-categories/', BlogCategoryAPIView.as_view(), name='blog-category'),
    path('blog-categories/<int:pk>', BlogCategoryAPIView.as_view(), name='blog-category'),
]
