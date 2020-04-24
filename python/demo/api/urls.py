from django.urls import path
# from api.views import categories_list, category_detail
# from api.views.views_cbv import CategoryListAPIViews, CategoryDetailAPIViews
from rest_framework_jwt.views import obtain_jwt_token
from api.views.views_generic_short import CategoryListAPIView, CategoryDetailAPIView
from api.views.views_generic_short import ProductListAPIView, CategoryWithProductSerializer

urlpatterns = [
    # path('categories/', categories_list),
    # path('categories/<int:category_id>', category_detail),
    # path('categories/<int:category_id>/products', category_products),
    path('companies/', CategoryListAPIView.as_view()),
    # path('categories/<int:category_id>', CategoryDetailAPIView.as_view()),
    path('vacancies/', ProductListAPIView.as_view()),
    # path('products/,<int:category_id>', ProductListAPIView.as_view())
    # path('login/', obtain_jwt_token),
]
