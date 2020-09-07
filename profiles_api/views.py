from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

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