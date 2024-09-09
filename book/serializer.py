from rest_framework import serializers
from .models import Book
from author.serializer import AuthorSerializer
from author.models import Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        allow_null=False,
        required=True
    )

    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value):

        if Book.objects.filter(title=value).exists():
            raise serializers.ValidationError(
                'Book with this title already exists')

        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'Book price should be greater than 0')
        return value


class BookListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_author(self, obj):
        return AuthorSerializer(obj.author).data
