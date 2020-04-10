from django.urls import path
from api.views import categories_list


urlpatterns = [
    path('categories/', categories_list),
]