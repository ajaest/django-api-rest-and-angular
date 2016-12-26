from rest_framework import generics, permissions

from rest_framework import serializers
from .serializers import UserSerializer, PostSerializer, PhotoSerializer
from .models import User, Post, Photo
from .permissions import PostAuthorCanEditPermission

from django.contrib.auth import login, authenticate

import rest_framework.response as rest_response

import django.middleware.csrf

class UserMixin(object):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(UserMixin, generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(UserMixin, generics.RetrieveAPIView):
    lookup_field = 'username'


class PostMixin(object):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        PostAuthorCanEditPermission
    ]

    def perform_create(self, serializer):
        """Force author to the current user on save"""
        serializer.save(author=self.request.user)


class PostList(PostMixin, generics.ListCreateAPIView):
    pass


class PostDetail(PostMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class UserPostList(generics.ListAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super(UserPostList, self).get_queryset()
        return queryset.filter(author__username=self.kwargs.get('username'))


class PhotoMixin(object):
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoList(PhotoMixin, generics.ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class PhotoDetail(PhotoMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class PostPhotoList(generics.ListAPIView):
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = super(PostPhotoList, self).get_queryset()
        return queryset.filter(post__pk=self.kwargs.get('pk'))


class LoginServiceSerializer(serializers.Serializer):

    username = serializers.CharField(required=False, allow_null=True)
    password = serializers.CharField(required=False, allow_null=True)


class LoginAPIServiceView(
    generics.GenericAPIView
):
    short_description = 'API for logging users in'

    name = 'profile_restV1_login_service'

    allowed_methods = ('GET', 'POST')

    pagination_class = None

    serializer_class = LoginServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.post(request)

    def post(self, request, *args, **kwargs):

        user = authenticate()

        login(request, user)

        message = {
            'message': 'Logged in',
            'named_messages': {
                'csrftoken': django.middleware.csrf.get_token(request),
                'sessionid': request.session.session_key
            }
        }

        return rest_response.Response(message)