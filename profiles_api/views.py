from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """returns list of epi features"""

        an_apiview = [ 'uses http method as function (get , post, patch, put, delete'
                       'Is similar to a trad Django view',
                       'Gives you the most control over you application logic',
                       'Is mapped manually to URLs',
                 ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
