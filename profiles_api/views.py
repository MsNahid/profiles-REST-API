
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over the logic',
            'Is mapped manually to URLS',
        ]

        return Response(
            {
                'message': 'Hello!',
                'an_apiview': an_apiview,
            }
        )

    def post(self, request):
        """Create introduce message with your name and age"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            message = f" I'm Md.{name}.And i am {age} years old."
            return Response(
                {'message': message}
            )

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
       """Handle partial update of an object"""
       return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
       """Delete an object"""
       return Response({"method": "DELETE"})
