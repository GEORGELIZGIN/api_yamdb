from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.serializers import CurrentUserDefault
from .models import Title, Category, Genre
from django.contrib.auth import get_user_model

User = get_user_model()


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Category
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Genre
        lookup_field = 'slug'
