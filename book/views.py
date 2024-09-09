from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    def list(self, request):
        return Response("All books")
