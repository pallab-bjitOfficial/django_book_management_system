from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer, BookListSerializer
from rest_framework import status
from rest_framework import serializers
from author.serializer import AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):

    def list(self, request):
        book_list = Book.objects.all().select_related('author').order_by('-created_at')

        serializer = BookListSerializer(book_list, many=True)
        response_data = {
            'message': 'All Books',
            'data': serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        serializer = BookListSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
