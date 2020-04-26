from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from api.models import Company, Game, User, Category
from api.serializers import CompanyModelSerializer, GameModelSerializer, UserModelSerializer, CategoryModelSerializer2, \
    CategoryModelSerializer


class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer
    # permission_classes = (IsAuthenticated,)


class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer
    lookup_url_kwarg = 'company_id'


class GameListAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameModelSerializer


class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer2
    permission_classes = (IsAuthenticated,)


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_url_kwarg = 'category_id'
