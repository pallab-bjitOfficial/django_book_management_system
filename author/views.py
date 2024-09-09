from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response


class AuthorViewSet(viewsets.ModelViewSet):
    def list(self, request):
        return Response("All Authors")
