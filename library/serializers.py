from rest_framework import serializers
from .models import Author, Book, Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'bio']


    def create(self, validated_data):
        append_str = " the author" 
        validated_data['name'] += append_str  
        return super().create(validated_data)

    def update(self, instance, validated_data):
        append_str = " the author" 
        if 'name' in validated_data:
            validated_data['name'] += append_str  
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        append_str = "Mr/Mrs."  
        representation['name'] = append_str  + representation['name']
        return representation


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category' ,  'published_date']
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']