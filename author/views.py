from rest_framework import viewsets
from rest_framework.response import Response
from .models import Author
from .serializer import AuthorSerializer
from rest_framework import status


class AuthorViewSet(viewsets.ModelViewSet):
    def list(self, _):
        book_list = Author.objects.all()
        serializer = AuthorSerializer(book_list, many=True)
        response_data = {
            'message': 'All Authors',
            'data': serializer.data

        }
        return Response(response_data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, _, pk=None):
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(
            author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, _, pk=None):
        author = Author.objects.get(pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
