from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer, BookListSerializer
from rest_framework import status


class BookViewSet(viewsets.ModelViewSet):

    def list(self, _):
        book_list = Book.objects.all().select_related('author').order_by('-created_at')

        serializer = BookListSerializer(book_list, many=True)
        response_data = {
            'message': 'All Books',
            'data': serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = BookSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, _, pk=None):
        book = Book.objects.get(pk=pk)
        serializer = BookListSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(
            book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, _, pk=None):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
