from django.shortcuts import get_object_or_404
from django.views import generic
from rest_framework import mixins
from rest_framework import generics
from titles.models import Category, Title, Genre
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated, IsAdminUser)
from .serializers import (TitleSerializer, CategorySerializer,
                          GenreSerializer)
from .permissions import OwnerPermission


class CategoriesList(generic.ListView):
    template_name = 'categories_list.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()


class CategoryDetails(generic.DetailView):
    model = Category
    template_name = 'category_details.html'
    context_object_name = 'CategoryDetail'


class APICategory(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class APICategoryDetail(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'slug'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GenresList(generic.ListView):
    template_name = 'genres_list.html'
    context_object_name = 'genres'
    queryset = Genre.objects.all()


class APIGenres(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Genre.objects.all()
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


# class APIGenres(mixins.ListModelMixin,
#                 mixins.CreateModelMixin,
#                 mixins.DestroyModelMixin,
#                 generics.GenericAPIView):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     lookup_field = 'slug'
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name']
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class TitlesList(generic.ListView):
    template_name = 'titles_list.html'
    context_object_name = 'titles'
    queryset = Title.objects.all()


class APITitles(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, OwnerPermission)
    queryset = Title.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
