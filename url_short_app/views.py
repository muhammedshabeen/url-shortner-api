from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser, FormParser




class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if not username or not password or not email:
            return Response({"message": "Username, Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"message": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({"message": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "message": "User registered successfully.",
            "user_detail": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            },
            "token": token.key
        }, status=status.HTTP_201_CREATED)
    

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "message": "Login successful.",
                "user_detail":{
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                "token": token.key
            }, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)



class BlogCategoryAPIView(APIView):

    """API view to handle blog categories.
    Allows admin users to create, retrieve, update, and soft delete blog categories.
    """

    permission_classes = [IsAdminUser,IsAuthenticated()]

    def get_object(self, pk):
        return get_object_or_404(BlogCategory, pk=pk, soft_delete=False)

    def get(self, request):
        categories = BlogCategory.objects.filter(soft_delete=False)
        serializer = BlogCategorySerializer(categories, many=True)
        return Response({
            'message': "Blog categories retrieved successfully",
            "data": serializer.data
        },status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response({
                "message": "Blog category created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Invalid data",
            "errors": serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = BlogCategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Category updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "Invalid data",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        category = self.get_object(pk)
        category.soft_delete = True
        category.save()
        return Response({
            "message": "Category soft deleted successfully"
        }, status=status.HTTP_200_OK)



class BlogListCreateAPIView(APIView):
    """
    GET: List all blog posts (no authentication required).
    POST: Create a new blog post (admin only).
    """

    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsAdminUser()]
        return [AllowAny()]

    def get(self, request):
        """
        Return a list of all blog posts (soft_deleted=False).
        No authentication required.
        """
        slug_param = request.GET.get('slug', None)
        if not slug_param:
            blogs = Blog.objects.filter(soft_delete=False,is_published=True).order_by('-published_date')
            serializer = BlogListSerializer(blogs, many=True)
        else:
            try:
                blog = Blog.objects.get(soft_delete=False,is_published=True,slug=slug_param)
                serializer = BlogSerializer(blog)
            except Blog.DoesNotExist:
                return Response({"message": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
            
        return Response({
            "message": "Blog posts retrieved successfully", 
            "data": serializer.data
            },status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new blog post.
        Requires admin user.
        """
        print("DATA", request.data)
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response({"message": "Blog created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Invalid data", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    


class BlogDetailAPIView(APIView):
    """
    GET: Retrieve a blog post by ID (no authentication required).
    PUT: Update a blog post (admin only).
    DELETE: Soft delete a blog post (admin only).
    """
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsAuthenticated(), IsAdminUser()]
        return [AllowAny()]

    def get_object(self, pk):
        return get_object_or_404(Blog, pk=pk, soft_delete=False)


    def put(self, request, pk):
        """
        Update a blog post by ID.
        Requires admin user.
        """
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(updated_by=request.user)
            return Response({"message": "Blog updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid data", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Soft delete a blog post by ID.
        Requires admin user.
        """
        blog = self.get_object(pk)
        blog.soft_delete = True
        blog.save()
        return Response({"message": "Blog soft deleted successfully"}, status=status.HTTP_200_OK)

