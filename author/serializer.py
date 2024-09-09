from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def validate_name(self, value):
        if Author.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                'Author with this name already exists')
        return value
