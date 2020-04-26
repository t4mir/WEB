from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from api.views import viewsCBV, viewsFBV, viewsgeneric
from api.views.viewsgeneric import CompanyListAPIView, CompanyDetailAPIView, GameListAPIView, UserListAPIView, \
    CategoryListAPIView, CategoryDetailAPIView

urlpatterns = [

    path('login/', obtain_jwt_token),
    # path('categories/', viewsFBV.CategoryListView),
    path('companies/', viewsFBV.CompanyListView),
    path('categories/<int:category_id>', CategoryDetailAPIView.as_view()),
    path('games/', GameListAPIView.as_view()),
    path('games/<int:game_id>/', viewsCBV.GameDetailsView.as_view()),
    path('companies/<int:company_id>/', CompanyDetailAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),
    # path('categories/<int:category_id>/', viewsFBV.CategoryDetailsView),
    # path('categories/<int:category_id>/games/', viewsFBV.GamesListByCategory),
    path('categories/', CategoryListAPIView.as_view())
    # path('categories/', viewsFBV.GamesListView),

]
