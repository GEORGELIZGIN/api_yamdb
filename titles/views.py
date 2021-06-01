from django.shortcuts import get_object_or_404
from django.views import generic
from titles.models import Category, Title, Genre
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from .serializers import (TitleSerializer, CategorySerializer,
                          GenreSerializer)


class CategoriesList(generic.ListView):
    template_name = 'categories_list.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()


class CategoryDetails(generic.DetailView):
    model = Category
    template_name = 'category_details.html'
    context_object_name = 'CategoryDetail'


class APICategory(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Category.objects.all()
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class GenresList(generic.ListView):
    template_name = 'genres_list.html'
    context_object_name = 'genres'
    queryset = Genre.objects.all()


class APIGenres(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Genre.objects.all()


class TitlesList(generic.ListView):
    template_name = 'titles_list.html'
    context_object_name = 'titles'
    queryset = Title.objects.all()


class APITitles(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthenticated)
    queryset = Title.objects.all()
