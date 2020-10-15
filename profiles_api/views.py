from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns list of epi features"""

        an_apiview = [
            'uses http method as function (get , post, patch, put, delete'
            'Is similar to a trad Django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with your name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """"Hanle updating object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delte an update"""
        return Response({'methodemaaktnietuit': 'Delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'uses actions(list, create retrieve',
            'another one',
            'yesyes a line',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle getting an object by its ID"""
        return Response({'http_methode': 'GETE'})

    def update(self, request, pk=None):
        """handle updates"""
        return Response({'http_methode is ': 'UPDATE'})

    def partial_update(self, request, pk=None):
        """uitleg"""
        return Response({'httpmethode_aangeroepen': ' PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http methode': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """hanlde creating and updating profiels"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


